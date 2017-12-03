from django.contrib import admin

# Register your models here.

from .models import Person

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["first_name", "last_name"]
    class Meta:
        model = Person

admin.site.register(Person, PersonModelAdmin)
