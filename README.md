##EMENU - ONLINE RESTAURANT CARD SERVICE

> The project serves the possibility of browsing cards (menus) with the possibility of adding dishes along with their photos. 
> The service allows us to filter cards through three parameters "name", "add_date", "update_date" 
> and sorting this card using the parameters "name" and "dishes_counter".
> One of the tasks is to automatically send emails to registered users with newly added dishes and dishes
> which were modified the previous day.
> The project includes a Django Admin panel for content management. 

###Table of content

 - Technology stack
 - Instalation
 - Development
 - Docker
 - Test
 - Before commit ;)

###Technology Stack

 - Python 3.7
 - Django 3.0.3
 - Django Rest Framework 3.12.2
 - PostgresSql 12.4

###Instalation

Type in cmd
```
git clone https://github.com/dominikpogodzinski/api_exercise.git
```

Install requirements by 
```
pip install -r requirements.txt
```

### Development
```
* create local environment
* copy () to ()
* run docker-compose up to start PostgreSQL database
* run python manage.py migrate to create your database structure
* run python manage.py createsuperuser to create super user in database
* run python manage.py runserver to start server in development environment
```

### Docker start
```
$ docker-compose up
```

### Docker down
```
$ docker-compose down
```

###Test


###Before commit ;)

Before you send the code to the server, please runt this tests
```
$ python -m black --check -l 120 --exclude=venv .
$ python -m flake8 .
$ python -m isort --check-only --diff .
```
Part of errors you can fix running:
```
$ python -m black -l 120 --exclude=venv .
$ python -m isort .
```