from django.contrib.auth.models import AbstractUser
from django.db import models

class LibraryUser(AbstractUser):
    '''
    Custom user for our library project. Inherits from AbstractUser, which has the following
    fields:
        - username
        - first_name
        - last_name
        - email
        - is_staff
        - is_active
        - date_joined

    We add a birthdate field so that we can target events to patrons of specific ages and
    possibly restrict items that can be checked out.
    '''
    # Choices
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
            (MALE, 'Male'),
            (FEMALE, 'Female'),
            (OTHER, 'Other'),
    )

    # Fields
    # Birthdate is allowed to be null so that the superuser can be successfully created.
    # We validate that this is not null for other users in our ModelForm
    birthdate = models.DateField('Date of Birth', null=True, blank=False)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, blank=False)
    books = models.ManyToManyField('stacks.Book', through='stacks.LoanedBook')

    def __unicode__(self):
        return self.get_full_name()
