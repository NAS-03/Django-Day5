from django.urls import path
from user.views import StudentView,StudentAddView


urlpatterns = [
    path('',StudentView,name='students'),
    path('add/',StudentAddView,name='studentadd'),
]