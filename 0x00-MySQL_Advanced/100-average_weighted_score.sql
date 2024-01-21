-- Creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id_param INT)
BEGIN
	-- Declare variables for cursor
	DECLARE done INT DEFAULT 0;
	DECLARE total_weighted_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;
	DECLARE weight_score FLOAT;
	DECLARE proj_weight FLOAT;

	-- Declare cursor
	DECLARE cursor_projects CURSOR FOR
	SELECT c.score * p.weight, p.weight
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id_param;

	-- Declare continue handler
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	-- Open the cursor
	OPEN cursor_projects;

	-- Loop through the cursor
	weight_score_loop: LOOP
	
		-- Fetch data from the cursor into variables
		FETCH cursor_projects INTO weight_score, proj_weight;

		-- Check if there is no more data
		IF done = 1 THEN
			LEAVE weight_score_loop;
		END IF;

		SET total_weighted_score = total_weighted_score + weight_score;
		SET total_weight = total_weight + proj_weight;
	END LOOP weight_score_loop;

	-- Close the cursor	
	CLOSE cursor_projects;

	IF total_weight > 0 THEN
		-- Update the weighted score for the user and project
		UPDATE users
		SET average_score = total_weighted_score / total_weight
		WHERE users.id = user_id_param;
	END IF;
END $$

DELIMITER ;
