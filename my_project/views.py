from django.contrib.auth.models import User
from django.conf.urls import url
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome </h1>')

def delete(request):
    u = User.objects.get(username = "admin")
    u.delete()

    title = 'User deleted'
    html = '''<!DOCTYPE html>
    <html>
    <head>
        <title>''' + title + '''</title>
    </head>
    <body>
        <h1>User deleted</h1>
    </body>
    </html>'''
    return HttpResponse(html)

def add(request):
    user = User.objects.create_user('admin2', 'admin@admin.com', 'password')
    user.save()
    title = 'User added'
    html = '''<!DOCTYPE html>
    <html>
    <head>
        <title>''' + title + '''</title>
    </head>
    <body>
        <h1>User added</h1>
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
            <input type="button" value="Add" onclick="window.location.href='http://localhost:8000/add'"/>
            <input type="button" value="Delete" onclick="window.location.href='http://localhost:8000/delete'"/>
        </form>
    </body>
    </html>'''
    return HttpResponse(html)


urlpatterns = [
    url(r'^$', home),
    url(r'^delete/$', delete),
    url(r'^moderator/$', moderator),
    url(r'^add/$', add),
]
