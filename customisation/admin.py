from django.contrib import admin
from . import models


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ['image_tag']


class AccessoryRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date')
    ordering = ('-date',)


admin.site.register(models.Accessories, AccessoryAdmin)
admin.site.register(models.AccessoryRequest, AccessoryRequestAdmin)
