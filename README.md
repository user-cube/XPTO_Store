# XPTO Store

Online Shop Store made with django framework.

## Authors
* [Rui Coelho](https://github.com/user-cube/)

## Deploy on Heroku
Primeiro é preciso criar um Procfile:
```shell
echo 'web: gunicorn TPW_Proj1.wsgi' > Procfile
```
Alterar o ficheiro `settings.py` adicionando no topo:
```python
import django_heroku
```
E no final do documento acrescentar:
```python
django_heroku.settings(locals())
```
Adicionar aos requisitos:
```
django-heroku
```
## Migrate to PostgreSQL
In order to achieve that, do the following steps in order :
```shell script
$ python manage.py dumpdata > db.json
```
Change the database settings to new database such as of MySQL / PostgreSQL.
```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```
Note: We must create an .env file and add the following lines to `settings.py`
```python
from dotenv import load_dotenv
load_dotenv()
```
```shell script
$ python manage.py migrate
$ python manage.py shell
```
Enter the following in the shell
```python
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
```
After that we only need to load the previous dataset into the new database
```shell script
$ python manage.py loaddata db.json
```
