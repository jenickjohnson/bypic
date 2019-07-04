from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
from libstack.models import Category, Author,BookName

def error(request):
    return render(request,"error.html")
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        # return HttpResponse("iii")
        if username=="admin" and password=="adm123":
            return render(request,"stack.html",{})
        else:
            return render(request,"error.html",{})
def stack(request):
    return render(request,"stack.html")

def database(request):
    ao=Author.objects.all()
    return render(request,"database.html",{'a':ao})

def books(request):
    return render(request,"books.html")
def about(request):
    return render(request,"about.html")
def category(request):
    return render(request,'category.html')
def authorname(request):
    return render(request,'authorname.html')    
def publisher(request):
    return render(request,'publisher.html')
def bookname(request):
    return render(request,'bookname.html')        

def addauthor(request):
    if request.method=="POST":
        authorname=request.POST["authorname"]
        bookname=request.POST["bookname"]
        category=request.POST["category"]
        language=request.POST["language"]
        publisher=request.POST["publisher"]

        a=Author(authorname=authorname)
        a.save()

        cat=Category(category=category)
        cat.save()

        b=BookName(bookname=bookname,publisher=publisher,author=a,category=cat)
        b.save()
        bo=BookName.objects.all()

    return render(request,"addauthor.html", {})


