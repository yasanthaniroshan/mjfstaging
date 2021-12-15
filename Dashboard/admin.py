from django.contrib import admin
from .models import Cart,Order,Sales_records_total,Sales_records_individual


admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Sales_records_individual)
admin.site.register(Sales_records_total)
# Register your models here.
