CREATE TABLE csep2025(
   s_id SERIAL PRIMARY KEY,
   s_roll INT UNIQUE NOT NULL,
   firstname VARCHAR(50) NOT NULL,
   lastname VARCHAR(50) NOT NULL,
   department VARCHAR(10) NOT NULL,
   passyear NUMERIC(4,0) NOT NULL
);

CREATE TABLE {dept_name}_p{passout_year}_students (
   s_id SERIAL PRIMARY KEY,
   s_roll INT UNIQUE,
   firstname VARCHAR(50),
   lastname VARCHAR(50)
);

DROP TABLE {dept_name}_p{passout_year}_students;

CREATE TABLE faculties (
   f_id SERIAL PRIMARY KEY,
   f_serial INT UNIQUE,
   firstname VARCHAR(50),
   lastname VARCHAR(50),
   department VARCHAR(50)
);

DROP TABLE faculties;