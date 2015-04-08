from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LibraryUser
from stacks.admin import LoanedBookInline

@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):

    inlines = (LoanedBookInline,)

    def get_fieldsets(self, request, obj=None):
        return super(LibraryUserAdmin, self).get_fieldsets(request, obj) + (
                ('Custom Fields', {'fields': ('birthdate', 'gender')}),
        )
