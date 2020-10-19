from django.urls import path, include
from . import views
# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python

urlpatterns = [
    # localhost:/covid, get and post request for insert operation
    path('', views.covid_form, name='covid_insert'),
    # localhost:/covid/list, get and post request for retrive and display all records
    path('list/', views.covid_list, name='covid_list'),
    # localhost:covid/[id][covid_one], get and post request to update a record
    path('<int:id><int:covid_one>/', views.covid_form, name='covid_update'),
    # # localhost:covid/delete/[id], delete path
    path('delete/<int:id><int:covid_one>', views.covid_delete, name='covid_delete'),
    # # localhost:covid/covid_one, url to the display one record page
    path('covid_one/', views.covid_one, name='covid_one'),
    # # localhost:/covid/list/export,
    path('list/export', views.covid_export, name='covid_export'),
]
