#
# df = pd.read_excel('expedia_report_monthly_january_2018.xlsx', nrows=12)
#
# print(df.head())
#
# for index, row in df.iterrows():
#     month_int = row['Unnamed: 0'].month
#     month_name = datetime.date(1900, month_int, 1).strftime('%B')
#     year = row['Unnamed: 0'].year
#
#     print(f"{month_name}, {year} - Calls Offered: {row['Calls Offered']}")
#     print(f"{month_name}, {year} - Abandon after 30s: {row[' Abandon after 30s']}")
#     print(f"{month_name}, {year} - FCR: {row['FCR']}")
#     print(f"{month_name}, {year} - DSAT: {row['DSAT ']}")
#     print(f"{month_name}, {year} - CSAT: {row['CSAT ']}")
