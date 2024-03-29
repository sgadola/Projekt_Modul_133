# Generated by Django 2.2.7 on 2019-11-08 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(default='<Hier Name des Artikels einfügen>', max_length=20)),
                ('article_title', models.CharField(default='<Hier Titel des Artikels einfügen>', max_length=20)),
                ('article_content', models.CharField(default='<Hier Inhalt des Artikels einfügen>', max_length=500)),
                ('article_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
