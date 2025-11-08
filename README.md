# Django e Postgres com Docker

## Configurando o ambiente

### Customizando ALIASES do projeto (WSL/linux)

Esta etapa é opcional mas agiliza muito o trabalho uma vez que possibilita encurtar os comandos mais utilizados.
Deixei os mais comuns incluídos no arquivo ".bash_aliases" inclusive você pode personalizá-los com os comandos que desejar, neste projeto perceberá que "web" refere-se ao serviço configurado no "docker-compose.yml", caso tenha outros serviços ou prefira trocar o nome será necessário atualizar esta informação em todos os comandos deste arquivo. Para que o bash reconheça os comandos abra o arquivo de configurações do bash:

```bash
nano ~/.bashrc
```

Inclua o código abaixo no final do arquivo de configurações do mesmo:

```bash
if [ -f ./.bash_aliases ]; then
    source ./.bash_aliases
fi
```

Após inserir, pressione Ctrl + X para sair, depois Y e Enter para Salvar. Será necessário executar o comando para que as atualizações sejam aceitas:

```bash
source ~/.bashrc
```

Mesmo sem realizar essa customização, quando em execução dos containers, poderá executar os comando diretamente no bash do container atravez do comando:

```bash
docker-compose exec <service_name> <comandos>
```

Por exemplo, para criar um app chamado "loja", você utilizaria o seguinte:

```bash
docker-compose exec web python manage.py startapp loja
```

Lembrando mais uma vez que "web" é o nome dado ao serviço no docker-compose.yml

### Customizando o VSCode

Você encontrará dentro da pasta .vscode alguns arquivos que não vão para produção mas que podem auxiliar na sua produtividade, melhorando sua experiência com o Editor. Estes arquivos alteram apenas as preferencias do editor dentro deste projeto e podem ser personalizadas por você, escolhendo temas de cores, formatação automática ao salvar, entre outros.
