-- Creates a trigger to reset the attribute valid_email only when email has been changed
CREATE TRIGGER valid
AFTER UPDATE ON users
FOR EACH ROW
	UPDATE users
	SET valid_email = 0;
