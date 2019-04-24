# CS 192
#### This app  is made to translate languages in a really crude way.
##### The creators - Reyster, Allan, Cid

## Running guide for a TL2 computer

In terminal type
```
sudo pip install --upgrade pip
sudo pip install django
```
Download the git files
```
git clone https://github.com/cidazc/CS-192.git
cd CS-192/
```

Restart

Run the app
```
python manage.py runserver
```

Open up your browser to the URL:
```
localhost:8000
```


## Running guide

In terminal type
```
python manage.py runserver
```

Open up your browser to the link:
```
localhost:8000
```

### Create admin role

in terminal
```
python manage.py createsuperuser
```

### Saving new models

In terminal type
```
python manage.py makemigrations
python manage.py migrate
```


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

testing branches - make these so you wouldn't edit the master directly and to avoid breaking the main code
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
```


If you've made a mistake and want to revert back to an old commit
```
git reset --hard HEAD
git clean -n
git clean -f
```


## WINDOWS installation guide
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
