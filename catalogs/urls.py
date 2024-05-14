from django.urls import path
from . import views

app_name = 'catalogs'

urlpatterns = [
    path('show_rates/', views.show_rates, name='show_rates')
]
