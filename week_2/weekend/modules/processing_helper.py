import logging
import os
import sys
import pandas as pd
import phonenumbers
from email_validator import validate_email, EmailNotValidError


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


def check_data(row):
    """Runs data validation functions on each row

    Parameters
    ----------
    df : dataframe
        The input dataframe

    Returns
    ----------
    None
    """

    index = row.name
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
