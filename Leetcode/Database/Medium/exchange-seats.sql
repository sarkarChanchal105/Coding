/*

https://leetcode.com/problems/exchange-seats/

SQL Schema
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.


Mary wants to change seats for the adjacent students.


Can you write a SQL query to output the result for Mary?


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

select s_odd.id,s_even.student
from seat s_odd left join  seat s_even on s_odd.id=s_even.id-1
where
1=1
and mod(s_odd.id,2) <> 0
and mod(s_even.id,2) =0

union all

select s_even.id,s_odd.student
from seat s_odd right join  seat s_even on s_odd.id=s_even.id-1
where
1=1
and mod(s_odd.id,2) <> 0
and mod(s_even.id,2) =0

*/

-- create table seat (id int, student varchar2(20));



/*

insert into seat values(1,'Abbot');
insert into seat values(2,'Doris');
insert into seat values(3,'Emerson');
insert into seat values(4,'Green');
insert into seat values(5,'Jeames');

commit;
select * from seat

select * from seat;
*/


--create table seat (id int, student varchar2(20));


select s_odd.id,s_even.student
from seat s_odd  join  seat s_even on s_odd.id=s_even.id-1
where
1=1
and mod(s_odd.id,2) <> 0
and mod(s_even.id,2) =0

union all


select s_even.id,s_odd.student
from seat s_odd   join  seat s_even on s_odd.id=s_even.id-1
where
1=1
and mod(s_odd.id,2) <> 0
and mod(s_even.id,2) =0



union

select * from
(select s_odd.id,s_odd.student
from seat s_odd  left join  seat s_even on s_odd.id=s_even.id-1)a,
 (select count(1)c_count from seat )s

where s_even.id is null
--and mod(s_odd.id,2) <> 0
--and mod(s_even.id,2) =0
--and mod(s_odd.id,2) <> 0
--and mod(s_even.id,2) =0;
