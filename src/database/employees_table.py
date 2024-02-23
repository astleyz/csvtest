from sqlalchemy import Table, MetaData, Column, Integer, String, Date

metadata = MetaData()

employees_table = Table(
    "employees",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("surname", String),
    Column("address", String),
    Column("email", String),
    Column("phone", String),
    Column("date_of_birth", Date),
    Column("profession", String),
    Column("company", String),
    Column("country", String),
    Column("city", String),
)
