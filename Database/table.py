import psycopg2
from psycopg2 import errors
from connection import Credentials

# Base queries to create and delete tables in the database
create_query = """
    CREATE TABLE {dept_name}_p{passout_year}_students (
        s_id SERIAL PRIMARY KEY,
        s_roll INT UNIQUE,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    );
"""

delete_query = """
    DROP TABLE {dept_name}_p{passout_year}_students;
"""


# Begin the function to create table
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
        query = create_query.format(dept_name=dept_name, passout_year=passout_year)

        # Execute the query
        try:
            cur.execute(query)
            print("Table created successfully")
        except errors.DuplicateTable as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except errors.DuplicateTable:
        print("Table already exists")

    except Exception as e:
        print(e)

# Begin the function to delete table
def delete_table(dept_name, passout_year):
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
        query = delete_query.format(dept_name=dept_name, passout_year=passout_year)
        
        # Execute the query
        try:
            cur.execute(query)
            print("Table deleted successfully")
        except errors.ProgrammingError as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except errors.UndefinedTable:
        print("Table does not exists")

    except Exception as e:
        print(e)


# create_table('cse', 2025)
# delete_table('cse', 2025)