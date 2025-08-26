from django.contrib import admin

from apps.models import Planet

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'diameter', 'distance', 'description'
    list_display_links = 'title', 'diameter', 'distance', 'description'

