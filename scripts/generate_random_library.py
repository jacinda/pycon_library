#!/usr/bin/env python
# Script that generates some fake data for our library
import os, sys
sys.path.append(os.getcwd())
import django; django.setup()
import random

from stacks.models import Author, Book, LoanedBook

from faker import Factory
fake = Factory.create()

NUM_AUTHORS = 100
NUM_BOOKS = 300

# Create a series of fake authors; also create at least one book for each author
for x in range(NUM_AUTHORS):
    author = Author.objects.create(first_name=fake.first_name(), last_name=fake.last_name())
    b = Book.objects.create(
            call_number=fake.numerify(text="###.###"),
            page_count=fake.random_int(min=10, max=1001),
            title=' '.join(fake.words(nb=fake.random_int(1,6))).title(),
    )
    b.authors.add(author)
    b.save()

authors = Author.objects.all()
for x in range(NUM_BOOKS):
    author_set = set()
    for y in range(fake.random_int(1,3)):
        author_set.add(random.choice(authors))
    b = Book.objects.create(
            call_number=fake.numerify(text="###.###"),
            page_count=fake.random_int(min=10, max=1001),
            title=' '.join(fake.words(nb=fake.random_int(1,6))).title(),
    )
    for author in author_set:
        b.authors.add(author)
    b.save()
