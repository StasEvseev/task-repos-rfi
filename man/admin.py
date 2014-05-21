#coding: utf-8

from django.contrib import admin
from man.models import Man

class ManAdmin(admin.ModelAdmin):
    fields = ('name', 'follow_ids')
    list_display = ('name', 'follow_ids')

admin.site.register(Man, ManAdmin)