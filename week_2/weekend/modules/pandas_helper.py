import logging
logging.basicConfig(filename='output.log', format='%(asctime)s - %(levelname)s - %(message)s')

import pandas as pd


def display_dataframe(df, n=5):
    """Displays the first n rows of the dataframe

    Parameters
    ----------
    df : dataframe
        The input dataframe

    Returns
    ----------
    None
    """

    head = df.head(n)
    logging.info(head)


def groupby_size(df, col):
    """Groups dataframe by column and gets size

    Parameters
    ----------
    df : dataframe
        The input dataframe
    col : str
        The column name

    Returns
    ----------
    new_df : dataframe
        The output dataframe
    """

    try:
        new_df = pd.DataFrame({'count' : df.groupby([col]).size()}).reset_index()
        return new_df
    except:
        logging.error(f"Column: {col}, does not exist in this dataframe.")


def subset_df(df, cols):
    """Gets subset of dataframe

    Parameters
    ----------
    df : dataframe
        The input dataframe
    cols : list
        A list of columns

    Returns
    ----------
    new_df : dataframe
        The output dataframe
    """

    try:
        new_df = df[cols]
        return new_df
    except:
        logging.error("The column subset does not exist in this dataframe.")


def get_top_n(df, n):
    """Gets top n items in dataframe

    Parameters
    ----------
    df : dataframe
        The input dataframe
    n : int
        The number of items

    Returns
    ----------
    top_df : dataframe
        The output dataframe
    """

    try:
        sorted_df = df.sort_values(by='count', axis=0, ascending=False, inplace=False)
        top_df = sorted_df[:n]
        return top_df
    except:
        logging.error("Unable sort dataframe.")


def graph_bar_chart(df, x, y, filename):
    """Graphs dataframe as a bar chart

    Parameters
    ----------
    df : dataframe
        The input dataframe

    Returns
    ----------
    None
    """

    try:
        ax = df.plot.bar(x=x, y=y)
        export = f"./output/{filename}.jpg"
        ax.figure.savefig(export)
        return export
    except:
        logging.error("Unable to graph bar chart.")


def export_to_csv(df, name):
    """Exports dataframe to csv

    Parameters
    ----------
    df : dataframe
        The input dataframe
    name : str
        Name of the dataframe

    Returns
    ----------
    filename : str
        The filename of the CSV
    """

    try:
        filename = f"./output/{name}.csv"
        df.to_csv(filename)
        return filename
    except:
        logging.error('Unable to export dataframe to CSV file')
