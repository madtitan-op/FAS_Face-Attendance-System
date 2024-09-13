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


# Function to insert student data
def insert_student(dept_name, passout_year, s_roll, firstname, lastname):
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
        query = f"""
            INSERT INTO {dept_name}_p{passout_year}_students (s_roll, firstname, lastname)
            VALUES (%s, %s, %s);
        """
        student_data = (s_roll, firstname, lastname)

        # Execute the query
        try:
            cur.execute(query, student_data)
            print("Data inserted successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)

# Function to insert faculty data
def insert_faculty(f_serial, firstname, lastname, department):
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
        query = """
            INSERT INTO faculties (f_serial, firstname, lastname, department)
            VALUES (%s, %s, %s, %s);
        """
        faculty_data = (f_serial, firstname, lastname, department)

        # Execute the query
        try:
            cur.execute(query, faculty_data)
            print("Data inserted successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)


# Function to Update student data
def update_student(dept_name, passout_year, s_roll, firstname, lastname):
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
        query = f"""
            UPDATE {dept_name}_p{passout_year}_students
            SET firstname = %s, lastname = %s
            WHERE s_roll = %s;
        """
        student_data = (firstname, lastname, s_roll)

        # Execute the query
        try:
            cur.execute(query, student_data)
            print("Data updated successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)

# Function to Update faculty data
def update_faculty(f_serial, firstname, lastname, department):
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
        query = """
            UPDATE faculties
            SET firstname = %s, lastname = %s, department = %s
            WHERE f_serial = %s;
        """
        faculty_data = (firstname, lastname, department, f_serial)

        # Execute the query
        try:
            cur.execute(query, faculty_data)
            print("Data updated successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)


# Function to delete student data
def delete_student(dept_name, passout_year, s_roll):
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
        query = f"""
            DELETE FROM {dept_name}_p{passout_year}_students
            WHERE s_roll = %s;
        """
        student_data = (s_roll,)

        # Execute the query
        try:
            cur.execute(query, student_data)
            print("Student data deleted successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)

# Function to delete faculty data
def delete_faculty(f_serial):
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
        query = """
            DELETE FROM faculties
            WHERE f_serial = %s;
        """
        faculty_data = (f_serial,)

        # Execute the query
        try:
            cur.execute(query, faculty_data)
            print("Faculty data deleted successfully")
        except errors.UniqueViolation as e:
            print(e)
            cur.execute("ROLLBACK;")

        # Commit the transaction
        conn.commit()

        # Close the cursor & connection
        cur.close()
        conn.close()

    except Exception as e:
        print(e)


# Function to fetch student data
def get_student(dept_name, passout_year, s_roll):
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

        # Re-Write the query
        query = f"""
            SELECT * FROM {dept_name}_p{passout_year}_students
            WHERE s_roll = %s;
        """
        student_data = (s_roll,)

        # Execute the query
        cur.execute(query, student_data)
        data = cur.fetchone()

        # Close the cursor & connection
        cur.close()
        conn.close()

        return data

    except Exception as e:
        print(e)

#Function to fetch faculty data
def get_faculty(f_serial):
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

        # Re-Write the query
        query = """
            SELECT * FROM faculties
            WHERE f_serial = %s;
        """
        faculty_data = (f_serial,)

        # Execute the query
        cur.execute(query, faculty_data)
        data = cur.fetchone()

        # Close the cursor & connection
        cur.close()
        conn.close()

        return data

    except Exception as e:
        print(e)


# Function to fetch all student data
def get_all_students(dept_name, passout_year):
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

        # Re-Write the query
        query = f"""
            SELECT * FROM {dept_name}_p{passout_year}_students;
        """

        # Execute the query
        cur.execute(query)
        data = cur.fetchall()

        # Close the cursor & connection
        cur.close()
        conn.close()

        return data

    except Exception as e:
        print(e)

# Function to fetch all faculty data
def get_all_faculties():
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

        # Re-Write the query
        query = """
            SELECT * FROM faculties;
        """

        # Execute the query
        cur.execute(query)
        data = cur.fetchall()

        # Close the cursor & connection
        cur.close()
        conn.close()

        return data

    except Exception as e:
        print(e)