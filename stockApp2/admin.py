from django.contrib import admin
from .models import Stock, StockPrice

admin.site.register(Stock)
# admin.site.register(User)
admin.site.register(StockPrice)