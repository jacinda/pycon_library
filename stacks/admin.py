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


@admin.register(LoanedBook)
class LoanedBookAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_overdue', 'highlighted_due_date')
    list_select_related = ('book', 'patron')
