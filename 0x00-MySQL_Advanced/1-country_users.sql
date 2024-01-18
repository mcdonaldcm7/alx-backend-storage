-- Create a table `user` if it doesn't exists
CREATE TABLE IF NOT EXISTS user (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255),
	country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
