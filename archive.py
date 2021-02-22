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
