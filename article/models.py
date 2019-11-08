from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Article(models.Model):
    article_user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    article_name = models.CharField(max_length=20, default='<Hier Name des Artikels einfügen>')
    article_title = models.CharField(max_length=20, default='<Hier Titel des Artikels einfügen>')
    article_content = models.CharField(max_length=500, default='<Hier Inhalt des Artikels einfügen>')
