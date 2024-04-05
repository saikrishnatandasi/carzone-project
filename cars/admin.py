from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src = "{}" width="60" style="border-radius: 10px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id','thumbnail','car_title','city','colour','model','year','body_style','fuel_type','is_featured')
    list_display_links = ('id','thumbnail','car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','model','body_style','fuel_type','city')
    list_filter = ('city','fuel_type','body_style','model')

admin.site.register(Car,CarAdmin)
