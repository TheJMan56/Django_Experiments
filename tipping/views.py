from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

conn = sqlite3.connect('Books3.db', check_same_thread=False)
curs = conn.cursor()

# Create your views here.

class Book():
    def __init__(self):
        pass

    def newBook(self, bookID, title, author, publisher, description):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.publisher = publisher
        self.description = description

def Greeting(request):
    page = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(page)

def otherGreeting(request):
    return render(request, "greet.html", {"title": "greetings", "message": "hello world"})

def calculateTip(request):
    return render(request, "tipInput.html")

def displayTip(request):
    price = float(request.GET["price"])
    service = float(request.GET["service"])
    service /= 100
    amount = price + (price * service)
    return render(request, "tipOutput.html", {"amount": format(amount, ".2f")})

def addBook(request):
    return render(request, "books.html")

def addedBook(request):
    bookID = request.GET["bookID"]
    title = request.GET["title"]
    author = request.GET["author"]
    publisher = request.GET["publisher"]
    description = request.GET["description"]
    global book
    book = Book()
    book.newBook(bookID, title, author, publisher, description)
    return render(request, "addedBook.html", {"bookID": book.bookID, "title": book.title, "author": book.author, "publisher": book.publisher, "description": book.description})

def addBookToDatabase(request):
    bookID = request.GET["bookID"]
    title = request.GET["title"]
    author = request.GET["author"]
    publisher = request.GET["publisher"]
    description = request.GET["description"]
    ins = 'INSERT INTO Books (bookID, title, author,\
      publisher, description) \
      VALUES (?, ?, ?, ?, ?)'
    curs.execute(ins, (bookID, title, author, publisher, description))
    conn.commit()
    page = "<html><body><h1>Book added</h1></body></html>"
    return HttpResponse(page)

def outputBook(request):
    return render(request, "addedBook.html", {"bookID": book.bookID, "title": book.title, "author": book.author, "publisher": book.publisher, "description": book.description})