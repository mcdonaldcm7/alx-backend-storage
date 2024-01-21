-- Creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	-- Declare variables for cursor
	DECLARE done INT DEFAULT 0;
	DECLARE total_weighted_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;
	DECLARE cur_user_id INT;

	-- Declare cursor
	DECLARE cursor_projects CURSOR FOR
	SELECT c.user_id, SUM(c.score * p.weight), SUM(p.weight)
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	GROUP BY c.user_id;

	-- Declare continue handler
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	-- Open the cursor
	OPEN cursor_projects;

	-- Loop through the cursor
	weight_score_loop: LOOP
	
		-- Fetch data from the cursor into variables
		FETCH cursor_projects INTO cur_user_id, total_weighted_score, total_weight;

		-- Check if there is no more data
		IF done = 1 THEN
			LEAVE weight_score_loop;
		END IF;

		IF total_weight > 0 THEN
			-- Update the weighted score for the user and project
			UPDATE users
			SET average_score = total_weighted_score / total_weight
			WHERE users.id = cur_user_id;
		END IF;
	END LOOP weight_score_loop;

	-- Close the cursor	
	CLOSE cursor_projects;
END $$

DELIMITER ;
