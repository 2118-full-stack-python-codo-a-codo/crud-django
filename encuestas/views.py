from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def jhonathan(request):
    return HttpResponse("Respuesta creada por Jhonathan")

def Miguel(request):
    return HttpResponse("Respuesta creada por Miguel Royett")

def create(data):
    pass

def delete(data):
    pass

def read(data):
    return HttpResponse("READ Hello world from Django for Codo a Codo 4.0:"  )

def gretting(request):
    print(dict(request.GET))
   
    # Que hacemos si un GET?
    # vamos a escribir un IF para determinar si es GET la respuesta devuelve datos.
    #myUsers = User.objects.all() 
   #     output = []
    #     for user in myUsers:
    #    print(user.username)
    #    output.append(user.username)


    # Que hacemos si es un POST?
     #modificar la data
     #myNewUser = User()

    # Que hacemos si 

    myResponse = HttpResponse("Hello world from Django for Codo a Codo 4.0:"  )

    if request.method == "GET":
        myResponse = read(request)
    elif request.method == "UPDATE":
        myResponse = update(request)
    elif request.method == "QUE VA?":
        myResponse = delete(request)
    else: # Que method es?
        myResponse = create(request)

    return myResponse
