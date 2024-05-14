from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=25)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.char_code

    class Meta:
        verbose_name_plural = 'Currencies'

class Price(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField('Дата сбора данных')
    value = models.FloatField()

    def __str__(self):
        return f'Цена {self.value} рублей на {self.date}'
