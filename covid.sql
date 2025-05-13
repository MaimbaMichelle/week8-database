-- This SQL script sets up the database for tracking COVID-19 data

-- Create the table for storing COVID-19 cases data
CREATE TABLE covid_cases (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each record
    country VARCHAR(100),               -- Name of the country
    date DATE,                           -- Date when the data was reported
    cases INT,                           -- Number of confirmed cases
    deaths INT,                          -- Number of deaths
    recoveries INT                       -- Number of recoveries
);

-- Example of inserting sample data
INSERT INTO covid_cases (country, date, cases, deaths, recoveries) 
VALUES ('USA', '2020-01-01', 1000, 20, 500);

