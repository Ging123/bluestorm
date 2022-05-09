py -3 -m venv venv #create virtual enviroment
venv\Scripts\activate #activate virtual enviroment
python manage.py runserver
python manage.py startapp transactions
python manage.py migrate
python manage.py test
sqlite3 db.sqlite3

python manage.py test users.tests.create_user

INSERT INTO transactions_transaction (patient_id_id, pharmacy_id_id, quantity, date) VALUES(8, 8, 2000, '2019-12-16');

PRAGMA table_info(transactions_transaction);

SELECT * FROM transactions_transaction;

DELETE FROM pharmacies_pharmacy WHERE city = 'Rio Grande do Norte';