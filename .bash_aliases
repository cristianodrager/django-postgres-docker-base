alias manage='docker-compose exec web python manage.py'
alias runserver='docker-compose exec web python manage.py runserver'
alias makemig='docker-compose exec web python manage.py makemigrations'
alias mig='docker-compose exec web python manage.py migrate'
alias shell='docker-compose exec web python manage.py shell'
alias startapp='docker-compose exec web python manage.py startapp'
alias test='docker-compose exec web python manage.py test'
alias temp='docker-compose exec web apt-get install -y postgresql-client'


#PS1='\[\e[0;32m\]\W 👽 \[\e[0;32m\]'
PS1='👽 \[\e[0;32m\]\W $ \[\e[0m\]'

