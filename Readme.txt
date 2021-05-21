#Para inicial la base de datos y las migraciones


Before running the API we need to create the database. If the data base is created starting
on 1-. If the data is not created start from 4-8.

How to use it:
____________________________________________________

1. Erase __pycache__ files
2. Erase migration folder
3. Erase data.sqlite
____________________________________________________

4. Open the console:  export FLASK_APP=app.py ( set if you are using window)
5. Create the database by typing: flask db init
6. Create migrations by typing: flask db migrate -m "First Database"
7. Upgrade : flask db upgrade
___________________________________________

8. Run the application :  python app.py
____________________________________________________
DATABASE CHANGES:
1. If i want to add columns or do changes to my data base I change my models
3.I already have a dtabase  with flask db migrate -m "Changes in migration"
2.The go ahead and upgrade  : flask db upgrade


____________________________________________________
POSTMAN NOTES:

1. Its important to click the eye icon, set the global variables that you are going to be reusing and pasting them in the header with {{}} I did this with the Token
