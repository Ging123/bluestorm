py -3 -m venv venv #create virtual enviroment
venv\Scripts\activate #activate virtual enviroment
python manage.py runserver
python manage.py startapp transactions
python manage.py migrate
sqlite3 db.sqlite3