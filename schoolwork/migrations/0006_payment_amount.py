# Generated by Django 4.1.3 on 2023-02-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolwork', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(default=1000),
        ),
    ]