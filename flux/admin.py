from django.contrib import admin
from .models import Person, Heritage, Legacy

# Register your models here.

admin.site.register(Person)
admin.site.register(Heritage)
admin.site.register(Legacy)