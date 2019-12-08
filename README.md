# XPTO Store

Online Shop Store made with django framework.

## Main functionalities
* Login/logout made with built-in django authentication system.
* Admin panel to add, edit or delete items.
* List of all bought items by all costumers.
* List of "my purchases"
* Shopping cart
* Profile view
* Profile edit with picture upload
* Sign Up form

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
