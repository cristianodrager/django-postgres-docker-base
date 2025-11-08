#Django e Postgres com Docker
Quando em execução os containers poderá executar o comando a seguir para criar novos Apps:
- code: docker-compose exec web python manage.py startapp <nome_do_app>
* web é o nome dado ao serviço no docker-compose.yml
