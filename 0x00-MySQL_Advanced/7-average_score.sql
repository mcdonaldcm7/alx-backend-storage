-- Creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE average FLOAT;

	SELECT AVG(score) INTO average
	FROM corrections
	WHERE user_id = user_id;
END;

$$
