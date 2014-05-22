#coding: utf-8

from django.contrib import admin
from man.models import Man

class ManAdmin(admin.ModelAdmin):
    #fields = ('name', 'follow_ids')
    list_display = ('name', 'count_followers', 'count_follow')

admin.site.register(Man, ManAdmin)