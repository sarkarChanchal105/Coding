/*
https://leetcode.com/problems/monthly-transactions-ii/

SQL Schema
Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
Table: Chargebacks

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| trans_id       | int     |
| charge_date    | date    |
+----------------+---------+
Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
trans_id is a foreign key to the id column of Transactions table.
Each chargeback corresponds to a transaction made previously even if they were not approved.


Write an SQL query to find for each month and country, the number of approved transactions and their total amount, the number of chargebacks and their total amount.

Note: In your query, given the month and country, ignore rows with all zeros.

The query result format is in the following example:

Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 101  | US      | approved | 1000   | 2019-05-18 |
| 102  | US      | declined | 2000   | 2019-05-19 |
| 103  | US      | approved | 3000   | 2019-06-10 |
| 104  | US      | approved | 4000   | 2019-06-13 |
| 105  | US      | approved | 5000   | 2019-06-15 |
+------+---------+----------+--------+------------+

Chargebacks table:
+------------+------------+
| trans_id   | trans_date |
+------------+------------+
| 102        | 2019-05-29 |
| 101        | 2019-06-30 |
| 105        | 2019-09-18 |
+------------+------------+

Result table:
+----------+---------+----------------+-----------------+-------------------+--------------------+
| month    | country | approved_count | approved_amount | chargeback_count  | chargeback_amount  |
+----------+---------+----------------+-----------------+-------------------+--------------------+
| 2019-05  | US      | 1              | 1000            | 1                 | 2000               |
| 2019-06  | US      | 3              | 12000           | 1                 | 1000               |
| 2019-09  | US      | 0              | 0               | 1                 | 5000               |
+----------+---------+----------------+-----------------+-------------------+--------------------+

*/

drop table Transactions;
drop table Chargebacks;

create table  Transactions(id int, country varchar(4), state varchar(100), amount int, trans_date date);
create table  Chargebacks (trans_id int, trans_date date)

Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('101', 'US', 'approved', '1000', TO_DATE('2019-05-18','yyyy-mm-dd'));
insert into Transactions (id, country, state, amount, trans_date) values ('102', 'US', 'declined', '2000', TO_DATE('2019-05-19','yyyy-mm-dd'));
insert into Transactions (id, country, state, amount, trans_date) values ('103', 'US', 'approved', '3000', TO_DATE('2019-06-10','yyyy-mm-dd'));
insert into Transactions (id, country, state, amount, trans_date) values ('104', 'US', 'declined', '4000', TO_DATE('2019-06-13','yyyy-mm-dd'));
insert into Transactions (id, country, state, amount, trans_date) values ('105', 'US', 'approved', '5000', TO_DATE('2019-06-15','yyyy-mm-dd'));


Truncate table Chargebacks;
insert into Chargebacks (trans_id, trans_date) values ('102', to_date('2019-05-29','yyyy-mm-dd'));
insert into Chargebacks (trans_id, trans_date) values ('101', to_date('2019-06-30','yyyy-mm-dd'));
insert into Chargebacks (trans_id, trans_date) values ('105', to_date('2019-09-18','yyyy-mm-dd'));



select
to_char(trans.trans_date,'yyyy-mm') as month,
trans.country,
sum(case when state='approved' then 1 else 0 end) approved_count,
sum(case when state='approved' then amount else 0 end) approved_amount,
sum(case when state='chargeback' then 1 else 0 end) chargeback_count,
sum(case when state='chargeback' then amount else 0 end) chargeback_amount

from
(
select c.trans_id as id,t.country,'chargeback'as state,t.amount, c.trans_date
from chargebacks c left join transactions t on c.trans_id=t.id

union all

select * from transactions where state='approved'
)trans
group by
to_char(trans.trans_date,'yyyy-mm'), trans.country
