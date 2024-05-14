from datetime import datetime
from typing import Optional

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import DateForm
from .models import Currency, Price

from catalogs.models import Currency, Price

def show_rates(request: HttpRequest):
    date = request.GET.get('date')
    if date:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            prices = Price.objects.filter(date=date)
            return render(request, 'catalogs/index.html', {'prices': prices})
        except ValueError:
            return HttpResponse("Invalid date format", status=400)
    else:
        form = DateForm()
        return render(request, 'catalogs/index.html', {'form': form})