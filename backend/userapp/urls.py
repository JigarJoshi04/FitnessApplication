from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', signIn),
    path('signIn/', signIn, name="signIn"),
    path('signUp/', signUp, name="signup"),
    path('logout/', logout, name="log"),
    # path('accounts/', include('allauth.urls'))
]
