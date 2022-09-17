
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('login/',loginview),
    path('register/',register),
    path('logout/',logoutview),
]
