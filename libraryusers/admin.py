from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LibraryUser

@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        return self.fieldsets + (
                ('Custom Fields', {'fields': ('birthdate', 'gender')}),
        )
