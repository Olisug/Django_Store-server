# Generated by Django 4.2 on 2025-02-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Почтовый адрес'),
        ),
    ]
