import psycopg2
from psycopg2 import errors
from connection import Credentials

# CREATE STUDENT TABLE
create_query = """
    CREATE TABLE {dept_name}_p{passout_year}_students (
        s_id SERIAL PRIMARY KEY,
        s_roll INT UNIQUE,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    );
"""

# DELETE STUDENT TABLE
delete_query = """
    DROP TABLE {dept_name}_p{passout_year}_students;
"""

# DELETE FACULTY TABLE
delete_faculty_query = """
    DROP TABLE faculties;
"""


# Function to create student table
def create_student_table(dept_name, passout_year):
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

    except Exception as e:
        print(e)

# Function to delete student table
def delete_student_table(dept_name, passout_year):
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

# Function to create faculty table
def create_faculty_table():
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

        try:
            # CREATE FACULTY TABLE
            cur.execute("""
                CREATE TABLE faculties (
                    f_id SERIAL PRIMARY KEY,
                    f_serial INT UNIQUE,
                    firstname VARCHAR(50),
                    lastname VARCHAR(50),
                    department VARCHAR(50)
                );
            """)
            print("Table created successfully")
        except errors.DuplicateTable as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)

# Function to delete faculty table
def delete_faculty_table():
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

        # Execute the query
        try:
            cur.execute("DROP TABLE faculties;")
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
