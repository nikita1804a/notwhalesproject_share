from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField("Название", max_length=50)
    cost = models.IntegerField("Стоимость")
    image = models.ImageField("Картинка")

class Clients(models.Model):
    login = models.CharField("Логин", max_length=15)
    email = models.EmailField("Почта", max_length=50)
    phone_number = models.CharField("Телефон", max_length=11)
    password = models.CharField("Пароль", max_length=30, default='')
