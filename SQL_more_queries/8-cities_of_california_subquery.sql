-- 8-cities_of_california.sql
-- List all cities of California
USE hbtn_0d_usa;
SELECT cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';
