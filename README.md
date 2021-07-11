# crud-django

Correr linea de comando

`docker-compose run web django-admin startproject cruddjango .`


Ahora creamos una app que se llama encuestas

`docker-compose run web python manage.py startapp encuestas`


Cada vez que modifiquemos nuestro modelo de datos... vamos a correr el siguiente comando

`docker-compose run web python manage.py migrate`

Por ultimo creamos un super usuario

`docker-compose run web python manage.py createsuperuser`

