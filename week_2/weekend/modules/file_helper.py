import logging
import os
import sys
import csv
import glob
import datetime
import pandas as pd

reference_list = 'NYL.lst'


def get_csv_files():
    """Extracts all the CSV filenames in the current working directory

    Parameters
    ----------
    None

    Returns
    ----------
    files : list
        A list of the filenames
    """
    files = [file for file in glob.glob('*.csv')]

    if len(files) < 0:
        logging.error("There are no CSV files in this directory.")
        sys.exit(1)

    return files


def extract_date(filename):
    """Extracts all the CSV filenames in the current working directory

    Parameters
    ----------
    filename : str
        The CSV's filename

    Returns
    ----------
    date : str
        The date as a condensed string
    """

    try:
        stem = os.path.splitext(filename)[0]
        date = stem.split('_')[-1]
        return date
    except:
        logging.error("The file is the wrong format.")
        sys.exit(1)


def convert_date(date):
    """Converts date from a string representation to a datetime object

    Parameters
    ----------
    date : str
        The file's date

    Returns
    ----------
    date_obj : datetime
        The date as a datetime object
    """

    try:
        date_obj = datetime.datetime.strptime(date, '%Y%m%d')
        return date_obj
    except:
        logging.error("The filename does not have the right date format.")
        sys.exit(1)


def get_line_count(file):
    """Calculates the number of lines in a CSV

    Parameters
    ----------
    file : str
        The filename

    Returns
    ----------
    line_count : int
        The number of lines in the file
    """

    df = pd.read_csv(file)
    line_count = len(df.index)

    if line_count < 0:
        logging.error("There are no lines in this file.")
        sys.exit(1)

    return line_count


def check_line_variance(files):
    """Checks if the files are within 500 line variance

    Parameters
    ----------
    files : list
        A list of all the files

    Returns
    ----------
    None
    """

    if len(files) >= 2:
        last_file = files[-1]
        second_last_file = files[-2]
        lf_count = get_line_count(last_file)
        slf_count = get_line_count(second_last_file)
        diff = lf_count - slf_count
        diff_abs = abs(diff)

        if diff_abs > 500:
            logging.error("There are more than 500 lines in variance between the 2 files.")
            sys.exit(1)
    elif len(files) == 1:
        pass
    else:
        logging.error("There are no files to process.")
        sys.exit(1)


def open_reference_list():
    """Checks if reference file exists

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """

    global reference_list
    file_exists = os.path.isfile(reference_list)

    if not file_exists:
        create_reference_list()


def create_reference_list():
    """Create blank CSV file

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """

    with open('NYL.lst', 'w') as file:
        pass


def check_reference_list(filename):
    """Checks if file has already been processed

    Parameters
    ----------
    filename : str
        The name of the file

    Returns
    ----------
    None
    """

    with open('NYL.lst', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    unpacked_data = [record[0] for record in data]
    if filename in unpacked_data:
        logging.error("The file has already been processed.")
        sys.exit(1)


def update_reference_list(filename):
    """Adds filename after file has been processed

    Parameters
    ----------
    filename : str
        The name of the file

    Returns
    ----------
    None
    """

    with open('NYL.lst', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([filename])


def sort_files(files):
    """Sorts filenames by date

    Parameters
    ----------
    files : list
        A list of the string filenames

    Returns
    ----------
    ordered_files : list
        The filenames in descending date order
    """

    dates = [extract_date(file) for file in files]
    date_objs = [convert_date(date) for date in dates]
    file_tuple = list(zip(dates, files))
    file_tuple.sort(key=lambda tple:tple[0], reverse=True)
    ordered_files = [tple[1] for tple in file_tuple]
    return ordered_files
