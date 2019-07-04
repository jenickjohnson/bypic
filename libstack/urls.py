from django.conf.urls import include, url
from libstack.views import *
urlpatterns = [
    url('home/', home,name="home"),
    url('login/', login,name="login"),
    url('database/', database,name="database"),
    url('error/', error,name="error"),
    url('stack/', stack,name="stack"),
    url('books/', books,name="books"),
    url('about/', about,name="about"),
    url('category/', category,name="category"),
    url('authorname/', authorname,name="authorname"),
    url('bookname/', bookname,name="bookname"),        
    url('publisher/', publisher,name="publisher"),        
    url('addauthor/', addauthor,name="addauthor")

]