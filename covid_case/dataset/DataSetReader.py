from ..models import CovidCase
from ..forms import CovidForm
from csv import reader, writer
import os

# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python

workpath = os.path.dirname(os.path.abspath(__file__))
original_file = os.path.join(workpath, 'InternationalCovid19Cases.csv')


class DataSetReader:
    """
    This class should be working with any CSV file
    Updating on the __init__
    Function can be used when calling are: loadList, etc...
    """

    # Constructor

    def __init__(self):
        """
        The constructor for DataSetReader class.

        Parameters:
                file_name (str): The name of the csv file which should contains .csv extension.
        """

    # loadList will return a list reading from the given csv file, with given number fo rows to read
    def loadList(self, num_fetch, existing_list):
        """
        The function to open the file and creatinng CovidCases objects, and then
        return the result as a list objects.
        It is using Reader module.
        """
        li_cases = []
        print("original_file path: {}".format(original_file))
        try:

            with open(original_file) as csv_file:
                csv_reader = reader(csv_file)
                count = -1

                current_num_rows = existing_list.count()

                for row in csv_reader:
                    if count == num_fetch or current_num_rows == num_fetch:
                        break
                    if count > -1:
                        new_case = CovidCase(
                            country_id=row[0], date=row[1], cases=row[2],
                            deaths=row[3], name_fr=row[4], name_en=row[5])

                        li_cases.append(new_case)
                        current_num_rows += 1

                    count += 1

                if count < 0:
                    count = 0
                print("Number of rows affected {} ".format(count))
            # loading the list to the database

        except IOError as e:
            print("I/O error when reading file ({0}): {1}".format(e.errno, e.strerror))
        return li_cases

    def writeFile(self, covid_cases, out_file_name="ExportedFile.csv"):
        out_file_path = os.path.join(workpath, out_file_name)
        print("In Writting file")
        # Create your views here.
        # Author: The Dai Phong Le
        # Date: 2020-09-25
        # File name: CovidCase.py
        # Assignment 1 Python
        # READER

        if out_file_name != "ExportedFile.csv":
            raise IOError("file name must be ExportedFile.csv")

        for covid_case in covid_cases:
            print(covid_case.country_id)
        try:
            with open(out_file_path, "w") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow(["country_id", "date", "cases",
                                     "deaths", "name_fr", "name_en"])
                for case in covid_cases:
                    csv_writer.writerow([case.country_id, case.date, case.cases,
                                         case.deaths, case.name_fr, case.name_en])

        except IOError as e:
            print("I/O error when writting file ({0}): {1}".format(e.errno, e.strerror))
        return out_file_path


# Code nippet showing example how to use DataSetReader
# my_reader = DataSetReader("InternationalCovid19Cases.csv")
#
# # Using for loop for qualify assignment2
# for case in my_reader.loadList():
#     form = CovidForm(request.POST, instance=case)
#     if form.is_valid():
#         form.save()
