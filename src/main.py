#!/usr/bin/env python

"""
This app creates csv file and saves all rows in database
"""
# pylint: disable=C0413
import os
import csv
from itertools import islice
from dotenv import load_dotenv

load_dotenv()

from csv_data.generate import generate_fake_data
from database.employees_table import employees_table, metadata
from database.database_utils import get_connection, process_group
from utils.grouper import grouper


csv_filename = os.getenv("CSV_FILENAME")
csv_rows = int(os.getenv("ROWS_QUANTITY"))
row_group = int(os.getenv("ROWS_IN_PAGE"))
page_start = int(os.getenv("PAGE_START"))
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# generate csv file
generate_fake_data(csv_filename, csv_rows)
print("Csv file created successfully")

# connect to db and create table
connection = get_connection(db_user, db_password, db_host, db_name)
metadata.create_all(connection.engine)

with open(csv_filename, "r", encoding="utf8") as file:
    csvreader = csv.reader(file)
    next(csvreader)

    # define started row
    start_row = (page_start - 1) * row_group

    # split groups per ROWS_IN_PAGE and save using transaction
    for group in grouper(islice(csvreader, start_row, None), row_group):
        process_group(connection, employees_table, group)
    print("Database populated successfully")

connection.close()
