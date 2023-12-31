"""
URL configuration for studentdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='home'),
    path('students/',include('user.urls')),
    path('courses/',include('courses.urls')),

    # # For APIs
    # path('api/student/',include('user.api_urls')),
    # path('api/courses/',include('courses.api_urls')),

]
