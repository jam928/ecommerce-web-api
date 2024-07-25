# To run python migrations from the model classes
python manage.py migrate
python manage.py makemigrations

# To create a seperate feature folder
python manage.py startapp <--feature-->

# to add django to current folder
django-admin startproject <--name--> .

# to create super user after migration
python manage.py createsuperuser

# to run server
python manage.py runserverc