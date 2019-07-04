from django.db import models

    

class Author(models.Model):
    authorname=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
class BookName(models.Model):
    bookname=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)   
    author=models.ForeignKey('Author',on_delete=models.CASCADE) 
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
class Category(models.Model):
    category=models.CharField(max_length=200)
    
# class Book(models.Model):
#     bookname=models.CharField(max_length=200)
#     publisher = models.ForeignKey('Publisher')
#     author = models.ForeignKey('Author')
#     category=models.ForeignKey('Category')
#     language=models.ForeignKey('Language')
    #   lend_period = models.ForeignKey('LendPeriods')
# class LendPeriods(models.Model):
#     name=models.CharField(max_length=100)
#     days_amount=models.IntegerField()
#     class Meta:
#         get_latest_by="days_amount"
#         ordering=['days_amount']
#         verbose_name="Lending Period"
#         verbose_name_plural="Lending Periods"
    #   class Meta
    #     ordering=['title'] 
    #     verbose_name="Book"
    #     verbose_name_plural="Books" 
class addauthor(models.Model):
    addauthor=models.CharField(max_length=200)



