from datetime import datetime

from django.core.management.base import BaseCommand
import requests

from catalogs.models import Currency, Price


def load_currency_data():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)

    if response.status_code == 200:
        currency_data = response.json()
        return currency_data


class Command(BaseCommand):
    help = 'Загрузка данных курса валют'

    def handle(self, *args, **kwargs):
        currency_data = load_currency_data()
        if currency_data:
            datetime_string = currency_data.get('Date')
            datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S%z')
            for currency in currency_data.get('Valute').values():
                char_code = currency.get('CharCode')
                name = currency['Name']
                currency_entry, created = Currency.objects.get_or_create(
                    char_code=char_code,
                    name=name,
                    defaults={'char_code': char_code, 'name': name}
                )
                if created:
                    currency_entry.save()
                date = datetime_obj.date()
                nominal = currency.get('Nominal')
                value = currency.get('Value')
                if int(nominal) > 1:
                    value = float(value) / int(nominal)
                price_entry, created = Price.objects.get_or_create(
                    date=date,
                    value=value,
                    defaults={'date': date, 'value': value, 'currency': currency_entry}
                )
                if created:
                    price_entry.save()
            self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
        else:
            self.stdout.write(self.style.ERROR('Ошибка при загрузке данных'))
