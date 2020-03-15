/*
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key of this table.


Write an SQL query to find for each user, whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no.

It is guaranteed that no seller sold more than one item on a day.

The query result format is in the following example:

Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2019-01-01 | Lenovo         |
| 2       | 2019-02-09 | Samsung        |
| 3       | 2019-01-19 | LG             |
| 4       | 2019-05-21 | HP             |
+---------+------------+----------------+

Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2019-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2019-08-04 | 1       | 4        | 2         |
| 5        | 2019-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+

Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+

Result table:
+-----------+--------------------+
| seller_id | 2nd_item_fav_brand |
+-----------+--------------------+
| 1         | no                 |
| 2         | yes                |
| 3         | yes                |
| 4         | no                 |
+-----------+--------------------+

The answer for the user with id 1 is no because they sold nothing.
The answer for the users with id 2 and 3 is yes because the brands of their second sold items are their favorite brands.
The answer for the user with id 4 is no because the brand of their second sold item is not their favorite brand.

*/


drop table Users;
drop table  Orders;
drop table Items;

Create table  Users (user_id int, join_date date, favorite_brand varchar(10));
create table  Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int);
create table  Items (item_id int, item_brand varchar(10));

Truncate table Users;
insert into Users (user_id, join_date, favorite_brand) values ('1', to_date('2019-01-01','YYYY-MM-DD'), 'Lenovo');
insert into Users (user_id, join_date, favorite_brand) values ('2', to_date('2019-02-09','YYYY-MM-DD'), 'Samsung');
insert into Users (user_id, join_date, favorite_brand) values ('3', to_date('2019-01-19','YYYY-MM-DD'), 'LG');
insert into Users (user_id, join_date, favorite_brand) values ('4', to_date('2019-05-21','YYYY-MM-DD'), 'HP');

Truncate table Orders;
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', to_date('2019-08-01','YYYY-MM-DD'), '4', '1', '2');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', to_date('2019-08-02','YYYY-MM-DD'), '2', '1', '3');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', to_date('2019-08-03','YYYY-MM-DD'), '3', '2', '3');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', to_date('2019-08-04','YYYY-MM-DD'), '1', '4', '2');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', to_date('2019-08-04','YYYY-MM-DD'), '1', '3', '4');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', to_date('2019-08-05','YYYY-MM-DD'), '2', '2', '4');

Truncate table Items;
insert into Items (item_id, item_brand) values ('1', 'Samsung');
insert into Items (item_id, item_brand) values ('2', 'Lenovo');
insert into Items (item_id, item_brand) values ('3', 'LG');
insert into Items (item_id, item_brand) values ('4', 'HP');

commit;


/* Write your PL/SQL query statement below */


select U.user_id "seller_id"
,
case when secon_fav.item_brand is null or secon_fav.item_brand!=favorite_brand then 'no'
else 'yes' end as "2nd_item_fav_brand"
-- ,secon_fav.item_brand
-- ,favorite_brand

from Users U left join
(
select ord.seller_id, ord.item_id,It.item_brand
from
(
select seller_id,item_id,
rank() over (partition by seller_id order by order_date) rank_
from Orders
)Ord join Items It on It.item_id=Ord.item_id
where ord.rank_=2
)secon_fav on secon_fav.seller_id=U.user_id

order by 1



