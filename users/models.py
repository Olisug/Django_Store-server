from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    birth_date = models.DateField('Дата рождения',
                                  null=True,
                                  blank=True)
    email = models.CharField('Почтовый адрес',
                             max_length=50,
                             null=False,
                             blank=False)
