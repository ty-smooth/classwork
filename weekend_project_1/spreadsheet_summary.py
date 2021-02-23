"""Spreadsheet Summary Printer

This script allows the user to print important values from exported spreadsheets.

The script requires that `openpyxl` be installed within the Python environment.

"""

import sys
import logging
import openpyxl as xl
import datetime as dt


def get_month(cell_value):
    """Extracts the month integer and returns the text name of the month

    Parameters
    ----------
    cell_value : datetime
        The spreadsheet cell value containing the month of the column

    Returns
    ----------
    month_name : str
        The name of the month from the choosen cell
    """

    month_int = cell_value.month
    month_name = dt.date(1900, month_int, 1).strftime('%B').lower()
    return month_name


def get_year(cell_value):
    """Extracts the year and returns it

    Parameters
    ----------
    cell_value : datetime
        The spreadsheet cell value containing the month of the column

    Returns
    ----------
    year : str
        The year from the choosen cell
    """

    year_int = cell_value.year
    year = str(year_int)
    return year


def get_date(filename):
    """Extracts the month and year from the filename

    Parameters
    ----------
    filename : str
        The name of the file

    Returns
    ----------
    month : str
        The month of the file
    year : str
        The year of the file
    """

    split_filename = filename.split('_')
    month = split_filename[3]
    year = split_filename[4].split('.')[0]
    return month, year


def get_percentage(string):
    """Extracts the month and year from the filename

    Parameters
    ----------
    string : str
        The number as a decimal

    Returns
    ----------
    formatted_string : str
        The number as a percentage
    """
    formatted_string = "{:.2%}".format(string)
    return formatted_string

def main():
    logging.basicConfig(filename=f'expedia.log', level=logging.DEBUG)

    try:
        filename = sys.argv[1]
        file_month, file_year = get_date(filename)
    except:
        logging.error("The wrong file was provided.")
        sys.exit()

    wb = xl.open(filename)

    try:
        sheet1 = wb['Summary Rolling MoM']
        sheet2 = wb['VOC Rolling MoM']
    except:
        logging.error("The file does not have the right worksheets.")
        sys.exit()

    # Search row range for matching month, year value!!!
    for row in sheet1.iter_rows(min_row=2, max_row=13, max_col=6, values_only=True):
        month = get_month(row[0])
        year = get_year(row[0])

        if file_month == month and file_year == year:
            logging.info(f"{month}, {year} - Calls Offered: {row[1]:,}")
            logging.info(f"{month}, {year} - Abandon after 30s: {get_percentage(row[2])}")
            logging.info(f"{month}, {year} - FCR: {get_percentage(row[3])}")
            logging.info(f"{month}, {year} - DSAT: {get_percentage(row[4])}")
            logging.info(f"{month}, {year} - CSAT: {get_percentage(row[5])}")

    # Search col range for matching month, year value!!!
    for col in sheet2.iter_cols(min_row=0, max_row=9, min_col=2, max_col=24, values_only=True):
        month = get_month(col[0])
        year = get_year(col[0])

        if file_month == month and file_year == year:
            logging.info(f"{month}, {year} - Promoters: {col[3]}, {'Good' if col[3] > 200 else 'Bad'}")
            logging.info(f"{month}, {year} - Passives: {col[5]}, {'Good' if col[5] > 100 else 'Bad'}")
            logging.info(f"{month}, {year} - Detractors: {col[7]}, {'Good' if col[7] > 100 else 'Bad'}")

    print('Check log file for output')


if __name__ == "__main__":
    main()
