CREATE TABLE csep2025(
   s_id SERIAL PRIMARY KEY,
   s_roll INT UNIQUE NOT NULL,
   firstname VARCHAR(50) NOT NULL,
   lastname VARCHAR(50) NOT NULL,
   department VARCHAR(10) NOT NULL,
   passyear NUMERIC(4,0) NOT NULL
);