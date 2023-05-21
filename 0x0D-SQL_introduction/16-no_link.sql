-- Script lists all records of the table second_table if name is not null
SELECT score, cname FROM second_table WHERE cname IS NOT NULL ORDER BY score DESC;
