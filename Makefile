MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE)  test FortyTwoCoffeeCups

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE)  runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE)  syncdb --noinput

loaddata:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE)  loaddata fixtures/initial_data.json