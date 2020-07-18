from django.contrib import admin

# Register your models here.
from .models import Series, HistoricalData


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    pass
