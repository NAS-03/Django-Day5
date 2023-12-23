from django.urls import path
from courses.views import CourseView,CourseAddView


urlpatterns = [
    path('',CourseView,name='courses'),
    path('add/',CourseAddView,name='courseadd'),
    # path
]