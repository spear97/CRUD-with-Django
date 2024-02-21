# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date

# Find students with last name "Smith"
learners_smith = Learner.objects.filter(last_name='Smith')  # filter by last name 'Smith'
print("1. Find learners with last name `Smith`")
print(learners_smith)
print("\n")

# Order by dob descending, and select the first two objects
learners = Learner.objects.order_by('-dob')[:2]  # order by dob descending, select first two
print("2. Find top two youngest learners")
print(learners)
