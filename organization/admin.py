from django.contrib import admin
from .models import Organization, Team

class TeamInline(admin.TabularInline):
    """
    Team admin model
    """
    model = Team
    extra = 1

class OrganizationAdmin(admin.ModelAdmin):
    """
    Organiation admin
    """
    inlines = [TeamInline]
    list_display = ('name', 'created_at', 'updated_at', 'how_many_teams')

admin.site.register(Organization, OrganizationAdmin)
