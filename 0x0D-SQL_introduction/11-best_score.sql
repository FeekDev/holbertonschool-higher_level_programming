-- that lists all records with a score >= 10 in the tb_second.
-- Records should be ordered by score (top first).

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
