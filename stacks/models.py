from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    '''
    Model representing the author of a work.
    '''
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return ', '.join([self.last_name, self.first_name])


class AbstractItem(models.Model):
    '''
    Abstract base class representing common fields amongst the different types of items the
    library might keep in its stacks.
    The fine per day is not defined in the Abstract Base Class because that will be different for
    different types of items.
    '''
    call_number = models.CharField(
            max_length=100,
            help_text=_("Usually Dewey Decimal or Library of Congress classification."))
    # TODO: This would be better as a callable that automatically got the next item number
    item_number = models.PositiveIntegerField(
            default=1,
            help_text=_("If we have multiple copies of this book, a unique identifier for the item."))
    borrowing_period = models.PositiveIntegerField(
            default=14,
            help_text=_("Number of days this item can be borrowed before being renewed."))
    max_renewal_count = models.IntegerField(
            default=2,
            help_text=_("Maxmimum number of times this item can be renewed."))
    maximum_fine = models.DecimalField(
            max_digits=5, decimal_places=2, default='25.00',
            help_text=_("Maximum amount the patron will be fined for an overdue item. This is"
                        " usually the replacement cost of the item.")),
    authors = models.ManyToManyField(Author, related_name='works')

    class Meta:
        abstract = True
        unique_together = (('call_number', 'item_number'),)


class Book(AbstractItem):
    '''
    Model representing a book in the library's collection.
    Keeping this simple for the purposes of our example.
    Other fields we could have added include Publisher (probably M2M), publication date, ISBN,
    Edition, Format (e.g. hardcover, paperback), etc.
    '''
    page_count = models.PositiveIntegerField()
    title = models.CharField(max_length=4000)
    daily_fine = models.DecimalField(
            max_digits=4, decimal_places=2, default='0.25',
            help_text=_("Amount the patron will be fined per day for an overdue library book"))

    def __unicode__(self):
        return self.title


class LoanedBook(models.Model):
    '''
    Model representing an item that is on loan to a patron. It has a checkout-date and a relation
    to the patron and item that was checked out. The fine property is
    calculated based on the values for the due date and daily fine.

    A more complex example might have used generic foreign keys to represent the relationship
    between the loaned item and the library user. This could be an interesting
    project to try out for the hands-on portion.

    A more efficient implementation of fines would update this field with a daily job so that fine
    would be a field on the model.  This method would allow us to use database aggregate methods,
    which are more performant than doing this in Python.  The current implementation demonstrates
    the performance implications.
    '''
    patron = models.ForeignKey(settings.AUTH_USER_MODEL)
    book = models.ForeignKey(Book)

    checkout_date = models.DateField()
    due_date = models.DateField()
    # Return date is null until the item is checked in
    return_date = models.DateField(null=True)
    times_renewed = models.IntegerField(default=0)
    fine_paid = models.NullBooleanField()

    def __unicode__(self):
        return ': '.join([str(self.patron), str(self.book)])

    # TODO: Create this as a property
    def fine(self):
        # NOTE: Fine should not be larger than the total value of the item
        pass
