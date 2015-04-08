from django.contrib import admin

from .models import Author, Book, LoanedBook

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

admin.site.register(Book)
admin.site.register(LoanedBook)
