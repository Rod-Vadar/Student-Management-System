from django.urls import path
from . import views 
# the dot means import views from the current directory


urlpatterns = [
    path('', views.index, name='index'),
]
