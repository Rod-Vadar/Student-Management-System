from django.urls import path
from . import views 
# the dot means import views from the current directory


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
]
