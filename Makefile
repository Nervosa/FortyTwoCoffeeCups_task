MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=FortyTwoCoffeeCups_task.settings $(MANAGE)  test FortyTwoCoffeeCups

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=FortyTwoCoffeeCups_task.settings $(MANAGE)  runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=FortyTwoCoffeeCups_task.settings $(MANAGE)  syncdb --noinput

loaddata:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=FortyTwoCoffeeCups_task.settings $(MANAGE)  loaddata fixtures/initial_data.json