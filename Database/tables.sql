CREATE TABLE csep2025(
   s_id SERIAL PRIMARY KEY,
   s_roll INT UNIQUE NOT NULL,
   firstname VARCHAR(50) NOT NULL,
   lastname VARCHAR(50) NOT NULL,
   department VARCHAR(10) NOT NULL,
   passyear NUMERIC(4,0) NOT NULL
);

-- Create a student table wrt dept and passout year
CREATE TABLE {dept_name}_p{passout_year}_students (
   s_id SERIAL PRIMARY KEY,
   s_roll INT UNIQUE,
   firstname VARCHAR(50),
   lastname VARCHAR(50)
);

-- Delete a student table wrt dept and passout year
DROP TABLE {dept_name}_p{passout_year}_students;

-- Create faculty table
CREATE TABLE faculties (
   f_id SERIAL PRIMARY KEY,
   f_serial INT UNIQUE,
   firstname VARCHAR(50),
   lastname VARCHAR(50),
   department VARCHAR(50)
);

-- Delete faculty table
DROP TABLE faculties;

-- Insert a student
INSERT INTO {dept_name}_p{passout_year}_students (s_roll, firstname, lastname)
VALUES ({roll}, '{firstname}', '{lastname}');

-- Delete a student
DELETE FROM {dept_name}_p{passout_year}_students WHERE s_roll = {roll};

-- Update a student
UPDATE {dept_name}_p{passout_year}_students
SET firstname = {firstname}, lastname = {lastname}
WHERE s_roll = {roll};

-- Fetch a student
SELECT * FROM {dept_name}_p{passout_year}_students WHERE s_roll = {roll};

-- Fetch all students
SELECT * FROM {dept_name}_p{passout_year}_students;


-- Insert a faculty
INSERT INTO faculties (f_serial, firstname, lastname, department)
VALUES ({serial}, {firstname}, {lastname}, {dept});

-- Delete a faculty
DELETE FROM faculties WHERE f_serial = {serial};

-- Update a faculty
UPDATE faculties
SET firstname = {firstname}, lastname = {lastname}, department = {dept}
WHERE f_serial = {serial};

-- Fetch a faculty
SELECT * FROM faculties WHERE f_serial = {serial};

-- Fetch all faculties
SELECT * FROM faculties;