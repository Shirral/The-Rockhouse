from django.contrib import admin
from . import models


# Edit the display of RockAdoption objects in Django admin panel
class RockAdoptionAdmin(admin.ModelAdmin):
    readonly_fields = ('stripe_id', 'adoption_number')
    list_display = ('rock', 'user', 'date', 'adoption_number')
    ordering = ('-date',)


admin.site.register(models.RockAdoption, RockAdoptionAdmin)
