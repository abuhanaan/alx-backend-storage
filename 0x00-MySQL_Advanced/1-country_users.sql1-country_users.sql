-- Creates a table users with the following attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    country CHAR(2) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN')) 
);
