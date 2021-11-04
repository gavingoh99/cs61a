.read sp20data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest limit 20;

CREATE TABLE matchmaker AS
  SELECT a.pet as pet, a.song as song, a.color, b.color from students as a, students as b
  where a.pet = b.pet and a.song = b.song and a.time <> b.time;

CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
-- Insert all dogs into the stacks_helper table with stack_height and last_height
INSERT INTO stacks_helper
  SELECT name, height, height FROM dogs;
-- Insert dogs into the same rows if height of dogs being inserted > height of dogs previously inserted
-- Repeat until 4 dogs in stack
INSERT INTO stacks_helper
  SELECT dogs || , || name, stack_height + height, height FROM dogs,stacks_helper where height > last_height
INSERT INTO stacks_helper
  SELECT dogs || , || name, stack_height + height, height FROM dogs,stacks_helper where height > last_height
INSERT INTO stacks_helper
  SELECT dogs || , || name, stack_height + height, height FROM dogs,stacks_helper where height > last_height

-- Create a table by selecting stacks of dogs with stack_height > 170
CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper where stack_height > 170 order by stack_height;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*) <= 1 order by smallest;

CREATE TABLE sp20favpets AS
  SELECT pet, count(*) as count from students group by pet order by count DESC limit 10;


CREATE TABLE sp20dog AS
  SELECT pet, count from sp20favpets where pet = "dog";


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as count from students where seven = '7' group by instructor;