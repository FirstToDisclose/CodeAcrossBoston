from django.contrib import admin
from disclosures.models import Disclosure

class DisclosureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Disclosure, DisclosureAdmin)
