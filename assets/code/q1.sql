-- Q1:
-- 
-- (Adapted from Fall 2019) The scoring table has three columns, a player column of
-- strings, a points column of integers, and a quarter column of integers. The players
-- table has two columns, a name column of strings and a team column of strings.
-- Complete the SQL statements below so that they would compute the correct
-- result even if the rows in these tables were different than those shown. Important:
-- You may write anything in the blanks including keywords such as WHERE or
-- ORDER BY. Use the following table called courses for the questions below:
-- 
-- Q1 - Big Game
-- Tests
-- SELECT * FROM parta;
-- expect 1
-- expect 4
-- SELECT * FROM partb;
-- expect Cal|24
-- expect Stanford|20

CREATE TABLE scoring AS
    SELECT "Donald Stewart" AS player, 7 AS points, 1 AS quarter UNION
    SELECT "Christopher Brown Jr.", 7, 1 UNION
    SELECT "Ryan Sanborn", 3, 2 UNION
    SELECT "Greg Thomas", 3, 2 UNION
    SELECT "Cameron Scarlett", 7, 3 UNION
    SELECT "Nikko Remigio", 7, 4 UNION
    SELECT "Ryan Sanborn", 3, 4 UNION
    SELECT "Chase Garbers", 7, 4;
    
CREATE TABLE players AS
    SELECT "Ryan Sanborn" AS name, "Stanford" AS team UNION
    SELECT "Donald Stewart", "Stanford" UNION
    SELECT "Cameron Scarlett", "Stanford" UNION
    SELECT "Christopher Brown Jr.", "Cal" UNION
    SELECT "Greg Thomas", "Cal" UNION
    SELECT "Nikko Remigio", "Cal" UNION
    SELECT "Chase Garbers", "Cal";

CREATE TABLE parta AS
    SELECT ______________________________;

CREATE TABLE partb AS
    SELECT ______________________________;
