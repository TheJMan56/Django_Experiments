from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("say-hi", views.Greeting),
    path("hello-again", views.otherGreeting),
    path("got-bill", views.calculateTip),
    path("display", views.displayTip),
    path("books", views.addBook),
    path("addBook", views.addedBook),
    path("addBookToDatabase", views.addBookToDatabase),
    path("outputBook", views.outputBook),
]