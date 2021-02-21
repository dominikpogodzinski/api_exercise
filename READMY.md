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

### Docekr end
```
$ docker-compose down
```

### Entry to virtual machine
(musisz być w katalogu projektu)
```
$ docker-compose exec cs-web /bin/bash
```

### Testing
```
$ docker-compose exec cs-web ./test.sh
```

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