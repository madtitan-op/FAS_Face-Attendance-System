import psycopg2
from psycopg2 import errors
from connection import Credentials

# Write the base query to create the tables in the database
base_query = """
    CREATE TABLE {dept_name}_p{passout_year}_students (
        s_id SERIAL PRIMARY KEY,
        s_roll INT UNIQUE,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    );
"""
# Begin the function to create the tables
def create_table(dept_name, passout_year):
    try:

        # Connect with the db
        conn = psycopg2.connect(
            dbname = Credentials.dbname,
            user = Credentials.user,
            password = Credentials.password,
            host = Credentials.host,
            port = Credentials.port
        )

        # Create a cursor object
        cur = conn.cursor()
        cur.execute("BEGIN;")

        # Re-Write the query
        query = base_query.format(dept_name=dept_name, passout_year=passout_year)

        # Execute the query
        cur.execute(query)

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except errors.DuplicateTable:
        print("Table already exists")

    except Exception as e:
        print(e)

create_table('cse', 2025)