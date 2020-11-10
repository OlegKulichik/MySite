# Generated by Django 3.1.2 on 2020-11-01 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа: (оформляется/нет)')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Всеря добавления в карзину')),
                ('change_status', models.DateTimeField(auto_now=True, verbose_name='Время изменения статуса')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucket', to='item.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucket', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'db_table': 'bucket',
            },
        ),
    ]
