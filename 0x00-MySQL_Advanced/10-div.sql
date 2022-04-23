-- creates an index idx_name_first_score on the table names
-- and the first letter of name and the score.
-- Requirements:
-- Import this table dump: names.sql.zip
-- Only the first letter of name AND score must be indexed

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET result = a / b;
    END IF;
    RETURN result;
END $$
DELIMITER ;
