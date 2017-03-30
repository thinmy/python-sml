from django.contrib import admin
from tours.models import Tour

class TourAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tour, TourAdmin)
