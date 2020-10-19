from django.db import models
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python

# Create your models here.
# id,date,cases,deaths,name_fr,name_en
# AD,2020-03-03,1,0,Andorre,Andorra


class CovidCase(models.Model):
    # creating class model CovidCase
    country_id = models.CharField(max_length=2)
    date = models.CharField(max_length=20, blank=True, null=True)
    cases = models.CharField(max_length=10)
    deaths = models.CharField(max_length=10)
    name_fr = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
