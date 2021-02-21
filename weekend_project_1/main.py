import openpyxl as xl
import datetime
import logging

if __name__ == "__main__":
    user_input = input('Which month would you like to analyze: January or March? ')
    user_choice = 'january' if user_input.lower() == 'january' else 'march'
    filename = f'expedia_report_monthly_{user_choice}_2018.xlsx'
    logging.basicConfig(filename=f'{user_choice}.log', level=logging.DEBUG)

    wb = xl.open(filename)
    sheet1 = wb['Summary Rolling MoM']
    sheet2 = wb['VOC Rolling MoM']

    for row in sheet1.iter_rows(min_row=2, max_row=13, max_col=6, values_only=True):
        month_int = row[0].month
        month_name = datetime.date(1900, month_int, 1).strftime('%B')
        year = row[0].year

        logging.info(f"{month_name}, {year} - Calls Offered: {row[1]}")
        logging.info(f"{month_name}, {year} - Abandon after 30s: {row[2]}")
        logging.info(f"{month_name}, {year} - FCR: {row[3]}")
        logging.info(f"{month_name}, {year} - DSAT: {row[4]}")
        logging.info(f"{month_name}, {year} - CSAT: {row[5]}")

    for col in sheet2.iter_cols(min_row=0, max_row=9, min_col=2, max_col=24, values_only=True):
        month_int = col[0].month
        month_name = datetime.date(1900, month_int, 1).strftime('%B')
        year = col[0].year

        logging.info(f"{month_name}, {year} - Promoters: {col[3]}, {'Good' if col[3] > 200 else 'Bad'}")
        logging.info(f"{month_name}, {year} - Passives: {col[5]}, {'Good' if col[5] > 100 else 'Bad'}")
        logging.info(f"{month_name}, {year} - Detractors: {col[7]}, {'Good' if col[7] > 100 else 'Bad'}")
