from django.contrib import admin
from .models import Person

@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    name = Person.name
    title = Person.last_name