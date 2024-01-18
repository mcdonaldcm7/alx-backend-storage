-- Creates a trigger to reset the attribute valid_email only when email has been changed
DELIMITER $$
CREATE TRIGGER valid AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	SET @valid_email = 0;
END $$
