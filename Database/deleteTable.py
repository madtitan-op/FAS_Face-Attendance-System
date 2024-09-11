import psycopg2
from psycopg2 import errors
from connection import Credentials

# Write the base query to delete the tables in the database
base_query = """
    DROP TABLE {dept_name}_p{passout_year}_students;
"""
# Begin the function to delete the tables
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
        query = base_query.format(dept_name=dept_name, passout_year=passout_year)
        
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

delete_table('cse', 2025)