


"""

Allan Matthew B. Mariano 
2015-05804


“This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof.
 Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, 
 Diliman for the AY 2018-2019”.

"""





"""
MIT License

Copyright (c) 2019 Jose Carlos Rodrigo Azcarraga, Allan Mariano, Reyster Fresco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016.

Code History:
       -CID AZCARRAGA|FEB-7-2019| Creation of this Code
       -CID AZCARRAGA|FEB-*-2019| Addition of License, Code History, and other Information to Code
    
Information:
     file creation: This was generated February 7, 2019.
     development group: Salin - Group 2
     client group: CS 192 WFUV AY1819
     purpose: This generates the view and the main bulk of code that will be seen by the user

"""


from django.contrib.auth.models import User
from django.conf.urls import url
from django.http import HttpResponse
from my_project.models import Translation

def home(request):
    return HttpResponse('<h1> Welcome </h1>')

def delete(request):
    try:
        u = User.objects.get(username = "admin")
        u.delete()

        title = 'User admin deleted'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>User admin deleted</h1>
        </body>
        </html>'''
        return HttpResponse(html)
    except:
        title = 'Error'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>Error!!</h1>
        </body>
        </html>'''
        return HttpResponse(html)

def delete2(request):
    try:
        u = User.objects.get(username = "admin2")
        u.delete()

        title = 'User admin2 deleted'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>User admin2 deleted</h1>
        </body>
        </html>'''
        return HttpResponse(html)
    except:
        title = 'Error'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>Error!!</h1>
        </body>
        </html>'''
        return HttpResponse(html)

def add(request):
    try:
        user = User.objects.create_user('admin', 'admin@admin.com', 'password')
        user.save()
        title = 'User admin added'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>User admin added</h1>
        </body>
        </html>'''
        return HttpResponse(html)
    except:
        title = 'Error'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>Error!!</h1>
        </body>
        </html>'''
        return HttpResponse(html)
def add2(request):
    try:
        user = User.objects.create_user('admin2', 'admin@admin.com', 'password')
        user.save()
        title = 'User admin2 added'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>User  admin2 added</h1>
        </body>
        </html>'''
        return HttpResponse(html)
    except:
        title = 'Error'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>Error!!</h1>
        </body>
        </html>'''
        return HttpResponse(html)

def addTranslation(request):
    #try:
    b = Translation()
    b.origin_language = "Visaya"
    b.target_language = "Filipino"
    b.origin_text = "ambot"
    b.target_text = "ewan"
    b.context_examples = "ambot sa imo"
    b.upvotes = 69
    b.downvotes = 1
    b.save()

    title = 'Translation Added!'
    html = '''<!DOCTYPE html>
    <html>
    <head>
        <title>''' + title + '''</title>
    </head>
    <body>
        <h1>Translation added</h1>
    </body>
    </html>'''
    return HttpResponse(html)
    #except: 
    '''
        title = 'Error'
        html = <!DOCTYPE html>
        <html>
        <head>
            <title> + title + </title>
        </head>
        <body>
            <h1>Error!!</h1>
        </body>
        </html>
        return HttpResponse(html) 

    '''



def moderator(request):
    title = 'User added'
    html = '''<!DOCTYPE html>
    <html>
    <head>
        <title>''' + title + '''</title>
    </head>
    <body>
        <form>
            <input type="button" value="Delete admin" onclick="window.location.href='http://localhost:8000/delete'"/>
            <input type="button" value="Delete admin2" onclick="window.location.href='http://localhost:8000/delete2'"/>
            <input type="button" value="Add admin" onclick="window.location.href='http://localhost:8000/add'"/>
            <input type="button" value="Add admin2" onclick="window.location.href='http://localhost:8000/add2'"/>
        </form>
    </body>
    </html>'''
    return HttpResponse(html)


urlpatterns = [
    url(r'^$', home),
    url(r'^delete/$', delete),
    url(r'^delete2/$', delete2),
    url(r'^moderator/$', moderator),
    url(r'^add/$', add),
    url(r'^add2/$', add2),
    url(r'^add/$', addTranslation)

]
