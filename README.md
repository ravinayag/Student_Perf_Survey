# Student_Perf_Survey

Installation Notes :

1, Ensure you have Python 3.5 and > version
2, Install Django using pip

pip install django
user@~$ python -m django --version
2.2.1
user@~$  mkvirtualenv myproject
(myproject) user@~$ workon myproject

(myproject) user@~$ mkdir  djproject

(myproject) user@~$ cd djproject

(myproject) user@~/djproject$ django-admin startproject mysite

(myproject) user@~/djproject$ cd ./mysite

(myproject) user@~/djproject/mysite$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin,
 auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 19, 2019 - 15:29:54
Django version 2.2.1, using settings 'mysite.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
[19/May/2019 15:30:11] "GET / HTTP/1.1" 200 16348
[19/May/2019 15:30:11] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[19/May/2019 15:30:11] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[19/May/2019 15:30:11] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[19/May/2019 15:30:11] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[19/May/2019 15:30:11] "GET /favicon.ico HTTP/1.1" 404 1972
  
