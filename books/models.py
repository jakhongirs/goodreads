from django.db import models


# BOOK:
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)


# AUTHOR:
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()


# BOOK_AUTHOR:
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Book, on_delete=models.CASCADE)


# BOOK_REVIEW:
class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=Cascade)
