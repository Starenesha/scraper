import datetime

import requests
from django.core.management.base import BaseCommand

from main.models import Series

from main.models import HistoricalData


class Command(BaseCommand):
    help = 'Parse historical value'

    series = Series.objects.all()
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    def handle(self, *args, **options):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/41.0.2272.0 Safari/537.36'}

        for s in self.series:
            id_series = s.get_id_from_url
            r = requests.get("https://sbcharts.investing.com/events_charts/us/" + id_series + ".json", headers=headers).json()
            delete = [x.pop(-1) for x in r['data']]

            for list in r['data']:
                date = datetime.datetime.fromtimestamp(list[0] / 1e3)
                HistoricalData.objects.create(date=date, value=list[1], series=s)

            self.stdout.write('Success')
