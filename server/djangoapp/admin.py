from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'name', 'dealer_id', 'car_type', 'year']
    list_filter = ['car_type', 'car_make', 'dealer_id', 'year',]
    search_fields = ['car_make', 'name']


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)