-- Create Database and Table Default value Uniq auto gen id
-- Create Database and Table Default value Uniq auto gen id
SELECT id,name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name='California');
