"""Spreadsheet Summary Printer

This script allows the user to print important values from exported spreadsheets.

The script requires that `openpyxl` be installed within the Python environment.

"""

import openpyxl as xl
import datetime as dt
import logging

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
    month_name = dt.date(1900, month_int, 1).strftime('%B')
    return month_name

def analyze_sheet1(row):
    """Extracts key values from Sheet 1 and adds them to the log file

    Parameters
    ----------
    row : tuple
        The spreadsheet row values

    Returns
    ----------
    None : None
        Empty value as function does not need to return anything
    """

    month = get_month(row[0])
    year = row[0].year
    logging.info(f"{month}, {year} - Calls Offered: {row[1]}")
    logging.info(f"{month}, {year} - Abandon after 30s: {row[2]}")
    logging.info(f"{month}, {year} - FCR: {row[3]}")
    logging.info(f"{month}, {year} - DSAT: {row[4]}")
    logging.info(f"{month}, {year} - CSAT: {row[5]}")
    return None

def analyze_sheet2(col):
    """Extracts key values from Sheet 2 and adds them to the log file

    Parameters
    ----------
    col : tuple
        The spreadsheet column values

    Returns
    ----------
    None : None
        Empty value as function does not need to return anything
    """

    month = get_month(col[0])
    year = col[0].year
    logging.info(f"{month}, {year} - Promoters: {col[3]}, {'Good' if col[3] > 200 else 'Bad'}")
    logging.info(f"{month}, {year} - Passives: {col[5]}, {'Good' if col[5] > 100 else 'Bad'}")
    logging.info(f"{month}, {year} - Detractors: {col[7]}, {'Good' if col[7] > 100 else 'Bad'}")
    return None

def main():
    user_input = input('Which month would you like to analyze: January or March? ')
    user_choice = 'january' if user_input.lower() == 'january' else 'march'
    filename = f'expedia_report_monthly_{user_choice}_2018.xlsx'
    logging.basicConfig(filename=f'expedia_report_{user_choice}.log', level=logging.DEBUG)

    wb = xl.open(filename)
    sheet1 = wb['Summary Rolling MoM']
    sheet2 = wb['VOC Rolling MoM']

    sheet1_result = [analyze_sheet1(row) for row in sheet1.iter_rows(min_row=2, max_row=13, max_col=6, values_only=True)]
    sheet2_result = [analyze_sheet2(col) for col in sheet2.iter_cols(min_row=0, max_row=9, min_col=2, max_col=24, values_only=True)]
    print('Log file created')

if __name__ == "__main__":
    main()
