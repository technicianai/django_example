# django_example

This project exists to demo our product, Technician. Technician can automatically repair your code after a runtime exception is logged to Splunk, New Relic, or even a Slack channel.

## Running this Django application

1. Clone this repository.
2. Create a virtual environment.
```
python -m venv env
pip install -r requirements.txt
```
3. Make and apply migrations.
```
python manage.py makemigrations
python manage.py migrate
```
4. Run.
```
python manage.py runserver
```

