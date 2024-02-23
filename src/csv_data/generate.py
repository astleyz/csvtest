import csv
from faker import Faker


def generate_fake_data(filename: str, num_rows: int):
    """
    Create list of people and save to file
    :param filename: name of the file
    :param num_rows: quantity of rows in the file
    """
    fake = Faker()
    fieldnames = [
        "Name",
        "Surname",
        "Address",
        "Email",
        "Phone",
        "Date of birth",
        "Profession",
        "Company",
        "Country",
        "City",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_rows):
            writer.writerow(
                {
                    "Name": fake.first_name(),
                    "Surname": fake.last_name(),
                    "Address": fake.address(),
                    "Email": fake.email(),
                    "Phone": fake.phone_number(),
                    "Date of birth": fake.date_of_birth(),
                    "Profession": fake.job(),
                    "Company": fake.company(),
                    "Country": fake.country(),
                    "City": fake.city(),
                }
            )
