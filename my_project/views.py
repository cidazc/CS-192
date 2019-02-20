

"""

Allan Matthew B. Mariano 
2015-05804


“This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof.
 Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, 
 Diliman for the AY 2018-2019”.

"""




from django.contrib.auth.models import User
from django.conf.urls import url
from django.http import HttpResponse

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
    url(r'^add2/$', add2)

]
