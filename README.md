# Django e Postgres com Docker

## Configurando o Projeto

### Docker

Estamos utilizando os arquivos Dockerfile e docker-compose.yml para configurar o Docker através de scripts pré definidos. O docker-compose define um script para a estrutura geral de serviços dos containers, portas, volumes e outras configurações. Enquanto o Dockerfile está sendo utilizado para criar a imagem Python aonde o Django será executado. O Postgres roda utilizando uma imagem já existente e bastante popular, não sendo necessárias configurações adicionais.

### Criando e subindo os containers

Após configurados os arquivos de scripts e o Docker devidamente instalado é hora o docker-compose baixar as dependencias e iniciar os serviços executando o comando:

```bash
docker-compose up --build
```

Esta primeira execução utilizamos a flag --build para que tudo seja construído, sempre que for necessário alterar os arquivos Dockerfile ou docker-compose recomendo excluir os containers criados e repetir o comando acima, destaco que em alguns casos excluir as imagens também pode ser necessário. Após o build bem sucedido poderá executar sem a flag, automaticamente o projeto subirá mais rápido sem necessidade de baixar pacotes, criar imagens e containers.

```bash
docker-compose up
```

#### Comandos básicos para docker-compose

- up --build : cria e sobe os containers
- up : sobe os containers
- down : derruba o container
- exec : possibilita executar comandos no bash do container

Exemplo:

```bash
docker-compose exec <service_name> <comandos>
```

Ps. Os containers podem ser derrubados também via docker desktop ou no terminal em execução com o atalho: Ctrl + C

## Configurando o ambiente

Para facilitar a utilização de comandos e otimização da produção sugiro abaixo algumas customizações no ambiente de trabalho.

### Customizando o VSCode

Você encontrará uma pasta chamada .vscode com alguns arquivos que não vão para produção mas que podem auxiliar na sua produtividade, melhorando sua experiência com o Editor. Estes arquivos alteram apenas as preferencias do editor dentro deste projeto e podem ser personalizadas por você, escolhendo temas de cores, formatação automática ao salvar, entre outros...

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

Segue um exemplo, para criar um app chamado "loja", você utilizaria o seguinte:

```bash
docker-compose exec web python manage.py startapp loja
```

Lembrando mais uma vez que "web" é o nome dado ao serviço no docker-compose.yml

Com a personalização de alias esse comando encurta para:

```bash
startapp loja
```

#### Dica extra

Você pode personalizar seu terminal também editando esse arquivo, segue a minha configuração minimalista (exibindo apenas diretório atual e icone), basta adicionar uma linha abaixo da existente:

```bash
PS1='\[\e[0;32m\]\W 👽 \[\e[0m\]'
```

Procure por PS1 no documento e insira logo abaixo, você pode incluir # para ignorar linha caso queira realizar seus testes e personalizar ao seu gosto.

Ps. Para inserir emojis em qualquer lugar no Windows 11, pressione <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="16px" viewBox="0 0 24 24" width="26px" fill="#e3e3e3"><g><rect fill="none" height="24" width="24"/></g><g><g><path d="M11 11V3H5c-1.1 0-2 .9-2 2v6h8zm2 0h8V5c0-1.1-.9-2-2-2h-6v8zm-2 2H3v6c0 1.1.9 2 2 2h6v-8zm2 0v8h6c1.1 0 2-.9 2-2v-6h-8z"/></g></g></svg>+ .
