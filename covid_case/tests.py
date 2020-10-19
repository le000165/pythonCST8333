from django.test import TestCase
from .models import CovidCase
from .dataset.DataSetReader import DataSetReader
# Create your tests here.

# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python

# Models Test
# id,date,cases,deaths,name_fr,name_en

# Author: The Dai Phong Le
class CovidCaseTest(TestCase):
    print("Program by THE DAI PHONG LE")

    def create_CovidCase(self, country_id="TE", date="2020-01-01",
                         cases=99, deaths=99, name_fr="Test_fr", name_en="Test_en"):
        return CovidCase.objects.create(country_id=country_id, date=date, cases=cases,
                                        deaths=deaths, name_fr=name_fr, name_en=name_en)

    def update_CovidCase(self):
        update = CovidCase.objects.create(country_id="UP", date="2020-01-01", cases=99,
                                          deaths=99, name_fr="test update", name_en="test update")
        update.save()
        return update

    def test_CovidCase_creation(self):
        """Does the program read in records, placing data into correct fields of record objects?"""
        new_Covid = self.create_CovidCase()

        self.assertTrue(isinstance(new_Covid, CovidCase))
        self.assertEqual(new_Covid.country_id, "TE")

    def test_CovidCase_add(self):
        """Does the program add a new record into the sequential data structure?"""
        add_covid = self.create_CovidCase()
        add_covid.save()

        self.assertIn(add_covid, CovidCase.objects.all())

    def test_CovidCase_update(self):
        """Does the program update a record in the sequential data structure as expected?"""
        u_Covid = self.update_CovidCase()
        c = CovidCase.objects.get(country_id="UP")
        c.name_en = "New name"
        c.save()

        self.assertEqual(c.name_en, "New name")

    def test_CovidCase_delete(self):
        """Does the program remove a record from the sequential data structure as expected?"""
        # setting up by creating and saving the the database
        del_Covid = self.create_CovidCase()
        del_Covid.save()
        del_id = del_Covid.id
        # we are going to delete by calling the delete function
        del_deleted = CovidCase.objects.get(id=del_id)
        del_deleted.delete()

        self.assertNotIn(del_Covid, CovidCase.objects.all())

    def test_file_error(self):
        """Does the program catch any exceptions or errors if the file is missing?"""
        my_reader = DataSetReader()
        covid_list = CovidCase.objects.all()

        with self.assertRaises(IOError):
            my_reader.writeFile(covid_list, "Not_A_File.csv")
