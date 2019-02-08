
"""

Allan Matthew B. Mariano 
2015-05804


“This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof.
 Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, 
 Diliman for the AY 2018-2019”.

"""

















"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_wsgi_application()
