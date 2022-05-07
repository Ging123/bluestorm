py -3 -m venv venv #create virtual enviroment
venv\Scripts\activate #activate virtual enviroment
python manage.py runserver
python manage.py startapp polls
python manage.py migrate