# Django e Postgres com Docker
Quando em execução os containers poderá executar os comando a seguir: 
- Para criar novos Apps:
docker-compose exec web python manage.py startapp <nome_do_app>
Onde web é o nome dado ao serviço no docker-compose.yml
- Para criar as migrações do DB:
docker-compose exec web python manage.py makemigrations
- Para executar as migrações em Banco:
docker-compose exec web python manage.py migrate
