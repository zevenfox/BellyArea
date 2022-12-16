# BellyArea

# Overview
BelleArea is a web server for seeing trend of obesity amoung people in different gender and age by collecting data from what food users choose to eat.

# Member
1. Kollawat Rupanya 6310545221 Faculty of software and knowledge engineering
2. Soravit Tangkulpanich 6310545396 Faculty of software and knowledge engineering
3. Sittanat Palakawong Na Ayudthaya 6310545400 Faculty of software and knowledge engineering

# Require libaries and tools
Python 3.8, 3.9, 3.10, and 3.11 or more
Django 4.1.1

# How to Install and Runserver (as a Developer)

1. Clone this project repository to your local machine
    ````
    git clone https://github.com/jaybjackie/HungryMe.git
    ````
2. Go to  this repository directory<br>
   
   for `MacOS/Linux`
   ````
   cd HungryMe
   ````
   
    
3. Install required packages.

    ````
    pip install -r requirements.txt
    ````

4. Modify `sample.env` by the following lines:

    To create SECRET KEY
    ```
    python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())'
    ```

    Put the SECRET KEY in .env file

    ```
    SECRET_KEY = 'YOUR-SECRET-KEY'
    DEBUG = False
    ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
    ```

5. Migrate the database.

    for `MacOS/Linux`
    ````
    python manage.py migrate
    ````

6. Importing data from `data.json`.
    ````
    python manage.py loaddata data.json
    ````
7. Run the server.
 
   for `MacOS/Linux`
   ````
   python manage.py runserver
   ````
 
 Go to the app:
[http://localhost:8000/](http://localhost:8000/)

## DEMO run
You can uses these demo users below to visits the site.

| Email  | Password  |
|-----------|-----------|
|   test@gmail.com  | test1234 |
