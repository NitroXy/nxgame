Requirements: django_cas_ng, django

Do this:

python manage.py migrate

Then do this:

python manage.py runserver 0.0.0.0:80 (where 0.0.0.0 is the allowed ip:s)
