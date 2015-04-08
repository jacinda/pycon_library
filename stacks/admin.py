from django.contrib import admin

from .models import Author, Book, LoanedBook


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Identifying Information', {
                'fields': ('title', 'page_count', 'authors', 'call_number', 'item_number')}),
            ('Loan Information', {
                'fields': ('borrowing_period', 'max_renewal_count', 'daily_fine', 'maximum_fine')}),
            )
    filter_horizontal = ('authors',)


class LoanedBookInline(admin.TabularInline):
    model = LoanedBook
    extra = 1


admin.site.register(LoanedBook)
