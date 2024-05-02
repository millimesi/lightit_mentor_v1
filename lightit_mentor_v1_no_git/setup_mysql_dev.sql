-- script that prepares a MySQL server for the project:

-- creates the database 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS light_it_mentors_db;

-- creates user
CREATE USER IF NOT EXISTS 'mentors_dev'@'localhost' IDENTIFIED BY 'Million1234!';

-- Grant priviledge on the database to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON light_it_mentors_db.* TO 'mentors_dev'@'localhost';

-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'mentors_dev'@'localhost';
