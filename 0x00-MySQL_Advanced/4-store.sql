-- Creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER decr_quantity AFTER INSERT on orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END;
$$
DELIMITER ;
