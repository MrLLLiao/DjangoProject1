# from django.contrib import admin
#
# # Register your models here.
#
# from login.models import Siteuser
# class SiteuserAdmin(admin.ModelAdmin):
#     list_display = ['name', 'gender']
#     list_filter = ['name']
#     list_per_page = 2
#     list_display_links = ['name']
# admin.site.register(Siteuser, SiteuserAdmin)

from django.contrib import admin
from .models import Siteuser

class SiteuserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'gender', 'creat_time', 'last_login_time']
    list_filter = ['gender', 'creat_time']
    search_fields = ['username', 'email']  # 让 admin 可搜索
    ordering = ['-creat_time']             # 最新用户排在最前

admin.site.register(Siteuser, SiteuserAdmin)
