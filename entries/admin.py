from django.contrib import admin
from .models import Plans


# Register your models here.
@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['name_plan', 'status_plan']
# admin.site.register(Plans)

