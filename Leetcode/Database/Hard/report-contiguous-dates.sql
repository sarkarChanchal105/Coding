/*

https://leetcode.com/problems/report-contiguous-dates/
able: Failed

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| fail_date    | date    |
+--------------+---------+
Primary key for this table is fail_date.
Failed table contains the days of failed tasks.
Table: Succeeded

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| success_date | date    |
+--------------+---------+
Primary key for this table is success_date.
Succeeded table contains the days of succeeded tasks.


A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

Order result by start_date.

The query result format is in the following example:

Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+

Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+


Result table:
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+

The report ignored the system state in 2018 as we care about the system in the period 2019-01-01 to 2019-12-31.
From 2019-01-01 to 2019-01-03 all tasks succeeded and the system state was "succeeded".
From 2019-01-04 to 2019-01-05 all tasks failed and system state was "failed".
From 2019-01-06 to 2019-01-06 all tasks succeeded and system state was "succeeded".
*/

/* Write your PL/SQL query statement below */


Create table Failed (fail_date date);
Create table  Succeeded (success_date date);
Truncate table Failed;
insert into Failed (fail_date) values (to_date('2018-12-28','yyyy-mm-dd'));
insert into Failed (fail_date) values (to_date('2018-12-29','yyyy-mm-dd'));
insert into Failed (fail_date) values (to_date('2019-01-04','yyyy-mm-dd'));
insert into Failed (fail_date) values (to_date('2019-01-05','yyyy-mm-dd'));

insert into Succeeded (success_date) values (to_date('2018-12-30','yyyy-mm-dd'));
insert into Succeeded (success_date) values (to_date('2018-12-31','yyyy-mm-dd'));
insert into Succeeded (success_date) values (to_date('2019-01-01','yyyy-mm-dd'));
insert into Succeeded (success_date) values (to_date('2019-01-02','yyyy-mm-dd'));
insert into Succeeded (success_date) values (to_date('2019-01-03','yyyy-mm-dd'));
insert into Succeeded (success_date) values (to_date('2019-01-06','yyyy-mm-dd'));



SELECT period_state "period_state", trim(min(adate)) "start_date", trim(max(adate)) "end_date"

FROM
(
select status period_state, adate, adate - rank_ as origin_date, rank_ from
(
select Status,adate,rank() over(partition by Status order by adate) as rank_
from
(
select fail_date as adate, 'failed' as Status from Failed
where fail_date between to_date('2019-01-01','YYYY-MM-DD') and to_date('2019-12-31','YYYY-MM-DD')

union all
select success_date as adate, 'succeeded' as Status from Succeeded
where success_date between to_date('2019-01-01','YYYY-MM-DD') and to_date('2019-12-31','YYYY-MM-DD')
)A
)B
)C
group by origin_date,period_state
order by 2