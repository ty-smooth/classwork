## archive.py

for row in sheet1.iter_rows(min_row=2, max_row=13, max_col=6, values_only=True):
    month = get_month(row[0])
    year = row[0].year

    logging.info(f"{month_name}, {year} - Calls Offered: {row[1]}")
    logging.info(f"{month_name}, {year} - Abandon after 30s: {row[2]}")
    logging.info(f"{month_name}, {year} - FCR: {row[3]}")
    logging.info(f"{month_name}, {year} - DSAT: {row[4]}")
    logging.info(f"{month_name}, {year} - CSAT: {row[5]}")

people = [[80, 1.73], [55, 1.58], [49, 1.91]]
list(map(lambda x: bmi(x[0], x[1]), people))

bmi(80, 1.73)




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


def search_value_in_row_index(ws, file_month, file_year, row=1):
    for cell in ws[row]:
        try:
            month = get_month(cell.value)
            year = get_year(row[0])
            if month == file_month and year == file_year:
                return cell.column, row
        except:
            print('not a datetime cell')
            return None, row
