import logging
logging.basicConfig(filename='output.log', format='%(asctime)s - %(levelname)s - %(message)s')

import sys
sys.path.append('./modules/')

import os
import csv
import glob
import logging
import datetime

import pandas as pd
import numpy as np
import phonenumbers
from email_validator import validate_email, EmailNotValidError

from pandas_helper import display_dataframe, groupby_size, subset_df
from pandas_helper import get_top_n, graph_bar_chart, export_to_csv
from email_helper import send_email

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


def sort_files(dates, files):
    """Sorts filenames by date

    Parameters
    ----------
    dates : list
        A list of the datetime objects
    files : list
        A list of the string filenames

    Returns
    ----------
    ordered_files : list
        The filenames in descending date order
    """

    file_tuple = list(zip(dates, files))
    file_tuple.sort(key=lambda tple:tple[0], reverse=True)
    ordered_files = [tple[1] for tple in file_tuple]
    return ordered_files


def create_dataframe(file):
    """Creates a dataframe based on the CSV filename

    Parameters
    ----------
    file : str
        The CSV filename

    Returns
    ----------
    None
    """

    try:
        df = pd.read_csv(file)
        return df
    except:
        logging.error("Unable to read CSV with the pandas library.")
        sys.exit(1)


def fix_headers(df):
    """Renames the column headers

    Parameters
    ----------
    df : dataframe
        The input dataframe

    Returns
    ----------
    df : dataframe
        The output dataframe
    """

    df = df.rename(columns={'Agent Writing Contract Start Date (Carrier appointment start date)':
                            'Agent Writing Contract Start Date',
                            'Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)':
                            'Agent Writing Contract Status'}, errors='ignore')
    return df


def check_data(df):
    """Iterates through dataframe and runs data validation functions

    Parameters
    ----------
    df : dataframe
        The input dataframe

    Returns
    ----------
    None
    """

    for index, row in df.iterrows():
        phone_one = 'Agency Phone Number'
        phone_two = 'Agent Phone Number'
        validate_phone_number(row[phone_one], phone_one, index)
        validate_phone_number(row[phone_two], phone_two, index)

        state_one = 'Agency State'
        state_two = 'Agent State'
        validate_state(row[state_one], state_one, index)
        validate_state(row[state_two], state_two, index)

        email_one = 'Agent Email Address'
        validate_email_address(row[email_one], email_one, index)


def validate_phone_number(phone_number, col, index):
    """Checks if a phone number is valid

    Parameters
    ----------
    phone_number : str
        A phone number
    col : str
        The column name
    index : int
        The row index

    Returns
    ----------
    None
    """

    try:
        phone_number_obj = phonenumbers.parse(phone_number, 'US')
        if not phonenumbers.is_valid_number(phone_number_obj):
            logging.error(f"Index: {index}, Column: {col}, Not a valid US phone number.")
    except:
        logging.error(f"Index: {index}, Column: {col}, Not a valid string or number for phone number.")


def validate_state(state, col, index):
    """Checks if a state abbreviation is valid

    Parameters
    ----------
    state : str
        A state abbreviation
    col : str
        The column name
    index : int
        The row index

    Returns
    ----------
    None
    """

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    try:
        if state not in states:
            logging.error(f"Index: {index}, Column: {col}, Not a valid US state abbreviation.")
    except:
        logging.error(f"Index: {index}, Column: {col}, No state given for this record.")


def validate_email_address(email, col, index):
    """Checks if an email address is valid

    Parameters
    ----------
    email : str
        An email address
    col : str
        The column name
    index : int
        The row index

    Returns
    ----------
    None
    """

    try:
      valid = validate_email(email)
    except EmailNotValidError as e:
      logging.error(f"Index: {index}, Column: {col}, Not a valid email address.")




def main():
    open_reference_list()
    files = get_csv_files()
    dates = [extract_date(file) for file in files]
    date_objs = [convert_date(date) for date in dates]
    sorted_files = sort_files(date_objs, files)
    check_line_variance(sorted_files)
    current_file = sorted_files[0]
    # check_reference_list(current_file)

    df = create_dataframe(current_file)
    df = fix_headers(df)
    # check_data(df)
    # update_reference_list(current_file)

    display_dataframe(df)
    df_2 = groupby_size(df, "Agency State")
    df_2_export = export_to_csv(df_2, 'agency_state_df')

    top_df = get_top_n(df_2, 10)
    chart_export = graph_bar_chart(top_df, 'Agency State', 'count', 'top_10_bar_chart')
    df_3 = subset_df(df, ["Agent Last Name", "Agent Middle Name", "Agent First Name",
                "Agent Writing Contract Start Date", "Date when an agent became A2O"])
    df_3_export = export_to_csv(df_3, 'subset_df')

    send_email('output.log', df_2_export, df_3_export, chart_export)

if __name__ == "__main__":
    main()
