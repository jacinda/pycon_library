from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LibraryUser

@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        return super(LibraryUserAdmin, self).get_fieldsets(request, obj) + (
                ('Custom Fields', {'fields': ('birthdate', 'gender')}),
        )
