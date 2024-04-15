from django.db import models


class RandomInteger(models.Model):
    value = models.IntegerField(
        verbose_name="значение",
    )
    updated_at = models.DateTimeField(
        verbose_name="последнее обновление",
        auto_now=True,
    )
