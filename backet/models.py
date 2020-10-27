from django.db import models
from user.models import TmsUser
from item.models import Item

class Bucket(models.Model):

    user = models.ForeignKey(TmsUser, on_delete=models.CASCADE, related_name="bucket") 
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bucket")
    status = models.BooleanField(default=True, verbose_name="Состояние-оформляется не оформляется")
    time = models.DateTimeField(verbose_name="Время резервации")

    class Meta:
        db_table = "bucket"
        verbose_name="Корзина"
        verbose_name_plural="Корзинаы"