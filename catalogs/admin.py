from django.contrib import admin

from .models import Currency, Price

admin.site.register(Currency)
admin.site.register(Price)
