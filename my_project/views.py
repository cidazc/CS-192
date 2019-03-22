


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
#from my_project.models import Translation

def home(request):
    #return HttpResponse('<h1> Welcome </h1>')
    try:
        html = '''<!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>My App</title>
            <script src="https://cdn.jsdelivr.net/npm/vue"></script>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <style>
              body{
                background-color: yellowgreen
              }
            </style>
          </head>
          <body>
            <div>
              <div class="jumbotron text-center">
                <h1>Salin</h1>
              </div>
              <div id="app">
                <h3>Log-in</h3>
                <input placeholder="Username">
                <input placeholder="Password">
                <br>
                <a href = "login.html">Log-in</a>
              </div>
              <script src="index.js"></script>
            </div>
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

def delete(request):
    try:
        u = User.objects.get(username = request)
        u.delete()

        title = 'User admin deleted'
        html = '''<!DOCTYPE html>
        <html>
        <head>
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>User ''' + request + '''deleted</h1>
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
        <h1> Moderator/Contributor Page </h1>
        <form>
            <input type="button" value="Delete admin" onclick="window.location.href='http://localhost:8000/accounts/remove_user'"/>
            <input type="button" value="Add User" onclick="window.location.href='http://localhost:8000/accounts/signup/'"/>
            <input type="button" value="Home" onclick="window.location.href='http://localhost:8000/'"/>
        </form>
    </body>
    </html>'''
    return HttpResponse(html)
