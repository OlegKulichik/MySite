# Generated by Django 3.1.3 on 2020-12-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201128_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='geeks_field',
            field=models.BooleanField(default=False),
        ),
    ]