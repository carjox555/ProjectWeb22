from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):

    return HttpResponse("Home")
def servicios (request):

    return HttpResponse("Servicios")
def tienda (request):

    return HttpResponse("Tienda")
def blog (request):

    return HttpResponse("Blogueersss")
def contacto (request):

    return HttpResponse("Contacto")