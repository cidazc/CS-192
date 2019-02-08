# CS 192

## WINDOWS installation guide 
he installers are found in the folder *installers or dependencies*

First, press clone or download from the github website.

### install python
run the installer
```
python-3.7.2-amd64.exe
```
### install pip

open command prompt and type
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### install virtualenv
open command prompt and type
```
pip install virtualenvwrapper-win
```
### install django
open command prompt and type
```
pip install django
```
### install git
run the installer
```
Git-2.20.1-64-bit.exe
```
### install github
run the installer
```
GitHubDesktopSetup.exe
```
## LINUX installation guide 
open the folder you want to store the files. Open up terminal and type

```
git clone https://github.com/cidazc/CS-192.git
```

### install django
open command prompt and type
```
pip install django
```

## running guide

open command prompt and type
```
python manage.py runserver
```

then open up your browser to the link:
```
localhost:8000
```
### create user

it will then ask you to log-in. But first you must create an account. To do that, close the webserver (CTRL + C). And go to terminal again and type
```
python manage.py createsuperuser
```
You will be then asked to choose a username, email, and password

Username: **admin**
Password: **password**

### delete user
```
 python manage.py shell
from django.contrib.auth.models import User
User.objects.get(username="admin", is_superuser=True).delete()
```
