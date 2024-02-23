# CSV Task

Creates a csv file with people, type of activity and other information about each person. Then the data will be parsed into a table in the database.

How to run, two ways:

- Start database in a docker containers (docker should be installed for this). In order to do this, execute `docker-compose up -d` command in the root directory.
- If you have installed PostgreSQL, set DB_USER, DB_PASSWORD, DB_NAME and reflect them in .env file
- Then execute main.py file `python3 src/main.py`
- In order to destroy database container execute `docker-compose down`
