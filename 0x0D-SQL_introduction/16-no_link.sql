-- script that lists all records of the table second_table.
-- Don’t list rows without a name value  score and the name (in this order)

INSERT INTO second_table () values(5, 'Aria', 18), (6, 'Aria', 12);
SELECT score, name FROM second_table ORDER BY score DESC;
