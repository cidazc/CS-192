# CS 192

**For sprint 2:(for the eyes of the team)**
*UX:*
-choose frontend (react, vue.js)
-add flow from log-in to user creation
-user creation: make a distinction between contributor and moderator
-moderator has special priviledges (deleting accounts, creating accounts)
-user creation: user can choose details (name, password etc.)
-flow: log-in (contributor) -> add translation as contributor
-flow2: log-in (contributor) -> search translation
-flow3: no log-in -> search translation
-UX design
-UX implementation

*Search:* (dito yung irereview ni mam yung 2 use cases natin)
-add translation feature (note all the info the database needs to store, work with DB person)
-search translation feature

*DB:*
-install postgre
-connect postgre and django
-make postgre work on github
-design table and schema
-code queries

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
