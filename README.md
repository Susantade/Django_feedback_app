# Django_feedback_app

**Introduction**
This is an app where anyone can write his/her own comment. For this, first he/she have to sign in (if his/her already has an account, otherwise first create an account). After succssful sign in he/she redirected to comment page, where he/she can leave a comment. In this page, he/she will also see other user's comments. There will be an **Filter** button, by clicking this button he/she will show the comments of only sign in (at that time) users.

**Requirements**
To run this app we require followings things:
- Django-4.0.2
- Python-3.9.7 
- Visual Studio Code editor
- MySQL Database
- XAMPP Server

**Run**
1. First create a database in XAMPP server with the same name as specified in the NAME key in DATABASES dictionary in settings.py file (in my case it is **comment1**).
2. Then open command prompt and go to the project folder and run **'python manage.py makemigrations'** for migrations.
3. After that run **'python manage.py migrate'** for migrate. After migrate a table will be created inside the database(in my case table name is **user**).
4. Then run **'python manage.py runserver [port_number]'** and server will be started. **'port_number'** is optional.
5. Then a link will be provided to us, and copy that link and open a browser and paste this link.
6. Then home page will show.
 
**Important Caustions**
- If css files will not work, then start server as **'python manage.py runserver --insecure'** or change default port(8000) as **'python manage.py runserver port_number'** . Because I change DEBUG = False for handle errors manually.
