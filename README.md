# CS 192

## Git guide

First time getting the git files
```
git clone https://github.com/cidazc/CS-192.git
```

Committing and pushing
```
git add .
git commit -m "your comment"
git push origin branchName
```

create a testing branch called new_branch_name
```
git checkout -b new_branch_name
```

move to branchName
```
git checkout branchName
git pull origin branchName
```

merging branchName with master
```
git checkout branchName
git merge -s ours master
git checkout master
git merge branchName


If you've made a mistake and want to revert back to an old commit
```
git reset --hard HEAD
```


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

## create admin role

open command prompt and type
```
python manage.py createsuperuser
```
