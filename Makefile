MANAGE=django-admin.py

test:
	python manage.py  test FortyTwoCoffeeCups

run:
	python manage.py  runserver

syncdb:
	python manage.py  syncdb --noinput

loaddata:
	python manage.py  loaddata fixtures/initial_data.json
