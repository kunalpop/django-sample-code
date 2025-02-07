from django.contrib import admin
from .models import City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ("unloc_code","name","country","province")
    list_filter = ("country","province","timezone",)

    

admin.site.register(City,CityAdmin)