import openpyxl as xl
import datetime

filename = 'expedia_report_monthly_january_2018.xlsx'
wb = xl.open(filename)
sheet1 = wb['Summary Rolling MoM']
sheet2 = wb['VOC Rolling MoM']

for row in sheet1.iter_rows(min_row=2, max_row=13, max_col=6, values_only=True):
    month_int = row[0].month
    month_name = datetime.date(1900, month_int, 1).strftime('%B')
    year = row[0].year

    print(f"{month_name}, {year} - Calls Offered: {row[1]}")
    print(f"{month_name}, {year} - Abandon after 30s: {row[2]}")
    print(f"{month_name}, {year} - FCR: {row[3]}")
    print(f"{month_name}, {year} - DSAT: {row[4]}")
    print(f"{month_name}, {year} - CSAT: {row[5]}")

for col in sheet2.iter_cols(min_row=0, max_row=9, min_col=2, max_col=24, values_only=True):
    month_int = col[0].month
    month_name = datetime.date(1900, month_int, 1).strftime('%B')
    year = col[0].year

    print(f"{month_name}, {year} - Promoters: {col[3]}, {'Good' if col[3] > 200 else 'Bad'}")
    print(f"{month_name}, {year} - Passives: {col[5]}, {'Good' if col[5] > 100 else 'Bad'}")
    print(f"{month_name}, {year} - Detractors: {col[7]}, {'Good' if col[7] > 100 else 'Bad'}")
