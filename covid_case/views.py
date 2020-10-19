from django.shortcuts import render, redirect
from .models import CovidCase
from .forms import CovidForm
from .dataset.DataSetReader import DataSetReader
import collections
# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python


def covid_list(request):
    """Loading a list of records at startup.

    Keyword arguments:
    request -- as default and required
    """
    # reading the file and loading 100 records to database
    # uncomment this to insert more data

    # Reading 100 records to database
    existing_covids = CovidCase.objects.all()
    print("Number of existing record are: {}".format(existing_covids.count()))
    print("Program By The Dai Phong Le")

    my_reader = DataSetReader()
    for case in my_reader.loadList(100, existing_covids):
        case.save()
    context = {'covid_list': CovidCase.objects.all()}
    return render(request, "covid_case/covid_list.html", context)


def covid_one(request):
    """ Loading the first row of the database to the page url

    Keyword arguments:
    request -- as default and required
    """
    covid_one = CovidCase.objects.first()
    context = {
        'id': covid_one.id,
        'country_id': covid_one.country_id,
        'date': covid_one.date,
        'cases': covid_one.cases,
        'deaths': covid_one.deaths,
        'name_fr': covid_one.name_fr,
        'name_en': covid_one.name_en,
    }

    return render(request, "covid_case/covid_one.html", context)


def covid_form(request, id=0, covid_one=1):
    """ at the covid form, for creating

    Keyword arguments:
    request -- as required
    id -- as for id
    covid_one -- to identify what page
    """
    # This is handling get operations
    if request.method == "GET":
        # if id is not set means 0 as default, we are having the get request to do insert operation
        if id == 0:
            # creating an empty form
            print("Creating an empty form")
            form = CovidForm()
        # otherwise we are having the update operation
        else:
            print("Getting an object at id = {} ready to edit form".format(id))
            # getting the object with the appropriate id
            covid = CovidCase.objects.get(pk=id)
            # creating the form with this object instance
            form = CovidForm(instance=covid)
        return render(request, "covid_case/covid_form.html", {'form': form})
    # This is hanlding the post operations when the user clicking on the button submit
    # Incore if else logic same as above to determine whether it is a insert or an update operations
    else:
        # When id==0 means submitting a new record
        if id == 0:
            form = CovidForm(request.POST)
        # otherwise submit a edit on an existing record
            print("Creating a new record")
        else:
            covid = CovidCase.objects.get(pk=id)
            form = CovidForm(request.POST, instance=covid)
            print("Updating a record at id = {}".format(id))

        if form.is_valid():
            result = form.save()
            print("1 row has been affected")
        else:
            print("form input error, it is not valid, nothing has been added")

        # If this is coming from covid_one page
        if covid_one == 0:
            place = redirect('/covid/covid_one')
        # otherwise process as normal list
        else:
            place = redirect('/covid/list')

    return place


# delete operation to handle delete a record from the database
def covid_delete(request, id, covid_one=0):
    """ at the covid delete, for deleting

    Keyword arguments:
    request -- as required
    id -- as for id
    covid_one -- to identify what page
    """
    print("Process to delete an object at id = {}".format(id))
    covid = CovidCase.objects.get(pk=id)
    result = covid.delete()
    print("Number of rows has been deleted = {}".format(result[0]))

    # If this is coming from covid_one page
    if covid_one == 0:
        place = redirect('/covid/covid_one')
    # otherwise process as normal list
    else:
        place = redirect('/covid/list')
    return place


# Export to a new csv file
def covid_export(request):
    """ at the covid export, for exporting file

    Keyword arguments:
    request -- as required
    """
    print("...In Exporting to a new file...")
    covid = CovidCase.objects.all()

    # for c in covid:
    #     print(c.country_id)

    my_reader = DataSetReader()

    new_file = my_reader.writeFile(covid)

    print("New file has been exported at location: {}".format(new_file))

    return redirect('/covid/list')
