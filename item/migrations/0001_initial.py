# Generated by Django 3.1.2 on 2020-10-27 17:50

from django.db import migrations, models
import item.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=20, verbose_name='Марка авто')),
                ('model', models.CharField(max_length=20, verbose_name='Модель авто')),
                ('body', models.CharField(max_length=20, verbose_name='Кузов авто')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('color', models.CharField(max_length=1, verbose_name='Цвет кузова')),
                ('cost', models.FloatField(verbose_name='Стоимость авто')),
                ('desc', models.TextField(verbose_name='Описание товара')),
                ('amount', models.IntegerField(verbose_name='Количество товара')),
                ('new', models.BooleanField(default=True, verbose_name='Состояние-ноый б/у')),
                ('photo', models.ImageField(upload_to=item.models.Item.load_photo, verbose_name='Фото авто')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'items',
            },
        ),
    ]