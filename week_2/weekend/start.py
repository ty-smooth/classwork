import logging
logging.basicConfig(filename='output.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

import sys
sys.path.append('./modules/')

from file_helper import get_csv_files, sort_files, check_line_variance
from file_helper import open_reference_list, check_reference_list, update_reference_list
from processing_helper import create_dataframe, fix_headers, check_data
from pandas_helper import display_dataframe, groupby_size, subset_df
from pandas_helper import get_top_n, graph_bar_chart, export_to_csv, create_name_col
from email_helper import send_email


def main():
    open_reference_list()
    files = get_csv_files()
    sorted_files = sort_files(files)

    current_file = sorted_files[0]
    check_line_variance(sorted_files)
    check_reference_list(current_file)
    df = create_dataframe(current_file)
    df = fix_headers(df)
    df = df.apply(lambda row: check_data(row), axis=1)
    update_reference_list(current_file)
    display_dataframe(df)

    df_group = groupby_size(df, "Agency State")
    display_dataframe(df_group)
    df_group_export = export_to_csv(df_group, 'agency_state_df')
    top_df = get_top_n(df_group, 10)
    chart_export = graph_bar_chart(top_df, 'Agency State', 'count', 'top_10_bar_chart')

    name_cols = ["Agent First Name", "Agent Middle Name", "Agent Last Name"]
    df = create_name_col(df, name_cols, "Agent Name")
    subset_cols = ["Agent Name", "Agent Writing Contract Start Date", "Date when an agent became A2O"]
    df_subset = subset_df(df, subset_cols)
    display_dataframe(df_subset)
    df_subset_export = export_to_csv(df_subset, 'subset_df')

    send_email('output.log', df_group_export, df_subset_export, chart_export)

if __name__ == "__main__":
    main()
