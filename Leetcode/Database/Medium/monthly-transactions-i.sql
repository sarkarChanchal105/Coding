/*

https://leetcode.com/problems/monthly-transactions-i/submissions/

SQL Schema
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].


Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

The query result format is in the following example:

Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+

Result table:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

*/

drop table Transactions;
create table  Transactions(id int, country varchar(4), state varchar(100), amount int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', TO_DATE('2018-12-18','yyyy-mm-dd'));
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', to_date('2018-12-19','YYYY-MM-DD'));
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', TO_DATE('2019-01-01','YYYY-MM-DD'));
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', TO_DATE('2019-01-07','YYYY-MM-DD'));


select
to_char(trans_date,'YYYY-MM') month,
country,
count(1) trans_count,
sum(case when state='approved' then 1 else 0 end) approved_count,
sum(amount) trans_total_amount,
sum(case when state='approved' then amount else 0 end) approved_total_amount

from transactions T

group by to_char(trans_date,'YYYY-MM'),country