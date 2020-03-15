/*
SQL Schema
Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key for this table.
title is the name of the movie.
Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key for this table.
Table: Movie_Rating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.


Write the following SQL query:

Find the name of the user who has rated the greatest number of the movies.
In case of a tie, return lexicographically smaller user name.

Find the movie name with the highest average rating in February 2020.
In case of a tie, return lexicographically smaller movie name.

Query is returned in 2 rows, the query result format is in the folowing example:

Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+

Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+

Movie_Rating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  |
| 2           | 2            | 2            | 2020-02-01  |
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  |
| 3           | 2            | 4            | 2020-02-25  |
+-------------+--------------+--------------+-------------+

Result table:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+

Daniel and Maria have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.


*/


Create table  Movies (movie_id int, title varchar(30));
Create table  Users (user_id int, name varchar(30));
Create table  Movie_Rating (movie_id int, user_id int, rating int, created_at date);
Truncate table Movies;

insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');

Truncate table Users;
insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'James');

Truncate table Movie_Rating;
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('1', '1', '3', to_date('2020-01-12','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('1', '2', '4', to_date('2020-02-11','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('1', '3', '2', to_date('2020-02-12','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('1', '4', '1', to_date('2020-01-01','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('2', '1', '5', to_date('2020-02-17','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('2', '2', '2', to_date('2020-02-01','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('2', '3', '2', to_date('2020-03-01','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('3', '1', '3', to_date('2020-02-22','YYYY-MM-DD'));
insert into Movie_Rating (movie_id, user_id, rating, created_at) values ('3', '2', '4', to_date('2020-02-25','YYYY-MM-DD'));


commit;

/* Write your PL/SQL query statement below */


select name as "results"
from
(
select U.name, count(distinct movie_id) count_
from Movie_Rating MR join Users U on MR.user_id=U.user_id
group by U.name
order by 2 desc, 1 asc
)B
where rownum<2

union all

select title
from
(
select M.title, avg(rating) avg_rating
from Movie_Rating MR join Movies M on MR.movie_id=M.movie_id
where created_at between to_date('2020-02-01','YYYY-MM-DD') and to_date('2020-02-29','YYYY-MM-DD')
group by M.title
order by 2 desc, 1 asc
)B
where rownum<2
