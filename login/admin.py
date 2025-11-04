from django.contrib import admin

# Register your models here.

from login.models import Siteuser
class SiteuserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']
    list_filter = ['name']
    list_per_page = 2
    list_display_links = ['name']
admin.site.register(Siteuser, SiteuserAdmin)