from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('remove_user/', views.remove_user, name = 'remove-user'),

]
