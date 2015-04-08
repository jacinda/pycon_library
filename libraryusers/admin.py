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

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, LoanedBookInline) and obj is None:
                continue
            yield inline.get_formset(request, obj), inline
