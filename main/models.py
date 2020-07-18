import re

from django.db import models

# Create your models here.


class Series(models.Model):
    title = models.CharField('title', max_length=300)
    url = models.CharField('url', max_length=200)

    def __str__(self):
        return self.title

    @property
    def get_id_from_url(self):
        url_id = re.search(r'\d{0,3}$', str(self.url)).group()
        return url_id


class HistoricalData(models.Model):
    date = models.DateTimeField('date')
    value = models.CharField('value',  max_length=20)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.series, self.date)
