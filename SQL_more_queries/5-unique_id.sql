-- 5-unique_id.sql
-- Create table unique_id with UNIQUE constraint on id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
