from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    """
    Organiation admin
    """
    exclude=("created_at", "updated_at")

admin.site.register(Organization, OrganizationAdmin)
