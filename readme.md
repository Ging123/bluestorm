py -3 -m venv venv #create virtual enviroment
venv\Scripts\activate #activate virtual enviroment
python manage.py runserver
python manage.py startapp transactions
python manage.py migrate
python manage.py test
sqlite3 db.sqlite3

python manage.py test users.tests.create_user

INSERT INTO patients_patient (name, last_name, birthday) VALUES('aa', 'bb', '2000-05-01')