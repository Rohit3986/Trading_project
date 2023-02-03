from django.contrib import admin
from .models import CsvFiles,Candles
# Register your models here.
admin.site.register(CsvFiles)
@admin.register(Candles)
class CandleAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Open','Date','High','Low','Close']
