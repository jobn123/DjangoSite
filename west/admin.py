from django.contrib import admin
from west.models import Character,Contact,Tag

# Register your models here.
# 管理页面过滤显示字段
# class ContactAdmin(admin.ModelAdmin):
#   fields = ('name', 'email')
# admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Contact, Tag])