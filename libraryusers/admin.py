from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LibraryUser

class LibraryUserAdmin(UserAdmin):
    pass

admin.site.register(LibraryUser, LibraryUserAdmin)
