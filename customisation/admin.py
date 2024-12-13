from django.contrib import admin
from . import models


# display visual previews of accessories in Django admin
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ['image_tag']


# see more information on the list of new accesory requests in Django admin
class AccessoryRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date')
    ordering = ('-date',)


admin.site.register(models.Accessories, AccessoryAdmin)
admin.site.register(models.AccessoryRequest, AccessoryRequestAdmin)
