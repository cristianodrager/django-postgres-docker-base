def validar_cpf(cpf: str) -> bool:
    # Remove caracteres especiais
    cpf = "".join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Rejeita CPFs com todos os números iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    # Compara com os dígitos informados
    return cpf[-2:] == f"{digito1}{digito2}"


def criar_cpf_valido() -> str:
    import random

    def calcular_digito(cpf_parcial):
        soma = sum(
            int(cpf_parcial[i]) * (len(cpf_parcial) + 1 - i)
            for i in range(len(cpf_parcial))
        )
        digito = (soma * 10) % 11
        return "0" if digito == 10 else str(digito)

    # Gera os primeiros 9 dígitos aleatórios
    cpf_parcial = "".join(str(random.randint(0, 9)) for _ in range(9))

    # Calcula os dois dígitos verificadores
    digito1 = calcular_digito(cpf_parcial)
    digito2 = calcular_digito(cpf_parcial + digito1)

    return cpf_parcial + digito1 + digito2


def hash_cpf(cpf):
    import os
    import hashlib
    import hmac

    secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
    cpf_hash = hmac.new(
        key=secret_key.encode(),
        msg=cpf.encode(),
        digestmod=hashlib.sha256,
    ).hexdigest()

    return cpf_hash
