Requirements: django_cas_ng, django


django_ca_ng's way of migrating stuff is still not updated to newest django version,
thus, before migrating for the first time, do this:

python manage.py makemigrations django_cas_ng

After that, you can simply do:

python manage.py migrate
