# CS 192

## installation guide
This installation only works for windows.

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
## running guide

open command prompt and type
```
python manage.py runserver
```

then open up your browser to the link:
```
localhost:8000
```

it will then ask you to log-in. But first you must create an account. To do that, close the webserver (CTRL + C). And go to terminal again and type
```
python manage.py createsuperuser
```
