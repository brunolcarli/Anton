install:
	pip install -r anton/requirements/common.txt

run:
	python manage.py runserver 0.0.0.0:4666 --settings=anton.settings.common

replit_pipeline:
	make install
	make run
