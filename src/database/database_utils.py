from sqlalchemy import create_engine
from tenacity import retry, stop_after_attempt, wait_fixed


def get_connection(db_user, db_password, db_host, db_name):
    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}")
    connection = engine.connect()
    return connection


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def process_group(connection, table, group):
    transaction = connection.begin()
    try:
        for row in group:
            if row is not None:
                insert_statement = table.insert().values(
                    name=row[0],
                    surname=row[1],
                    address=row[2],
                    email=row[3],
                    phone=row[4],
                    date_of_birth=row[5],
                    profession=row[6],
                    company=row[7],
                    country=row[8],
                    city=row[9],
                )
                connection.execute(insert_statement)
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        print("Error:", e)
        raise e
