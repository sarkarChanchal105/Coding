/*

https://leetcode.com/problems/restaurant-growth/

Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) have visited the restaurant.
amount is the total paid by a customer.


You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Write an SQL query to compute moving average of how much customer paid in a 7 days window (current day + 6 days before) .

The query result format is in the following example:

Return result table ordered by visited_on.

average_amount should be rounded to 2 decimal places, all dates are in the format ('YYYY-MM-DD').



Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         |
| 6           | Elvis        | 2019-01-06   | 140         |
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         |
| 1           | Jhon         | 2019-01-10   | 130         |
| 3           | Jade         | 2019-01-10   | 150         |
+-------------+--------------+--------------+-------------+

Result table:
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+

1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86

*/

{"headers":{"Customer":["customer_id","name","visited_on","amount"]},"rows":{"Customer":[[6,"Jaze","2019-01-04",130],
[32,"Newton","2019-01-04",80],[27,"Sakura","2019-01-04",130],[28,"Prudence","2019-01-05",150],[11,"Luffy","2019-01-05",70],
[41,"Josh","2019-01-05",60],[20,"Brock","2019-01-05",180],[23,"Sabo","2019-01-06",170],[23,"Sabo","2019-01-06",120],[21,"Mickey","2019-01-07",190],
[15,"Marti","2019-01-08",70],[3,"Maria","2019-01-08",150],[41,"Josh","2019-01-08",150],[18,"Jessie","2019-01-09",130],[3,"Maria","2019-01-09",80],
[6,"Jaze","2019-01-09",170],[4,"Winston","2019-01-09",130],[31,"Albert","2019-01-09",130],[4,"Winston","2019-01-09",140],
[4,"Winston","2019-01-09",180],[0,"Anna","2019-01-10",100],[30,"Halley","2019-01-10",80],[6,"Jaze","2019-01-10",150],[16,"Phoebe","2019-01-11",140],
[18,"Jessie","2019-01-11",50],[7,"khaled","2019-01-11",100],[31,"Albert","2019-01-11",190],[41,"Josh","2019-01-12",180],[28,"Prudence","2019-01-12",50],
[30,"Halley","2019-01-12",110],[6,"Jaze","2019-01-12",190],[0,"Anna","2019-01-13",80],[28,"Prudence","2019-01-14",160],[37,"Zeus","2019-01-14",70],
[41,"Josh","2019-01-14",200],[16,"Phoebe","2019-01-14",190],[7,"khaled","2019-01-14",200],[13,"Will","2019-01-14",110],[6,"Jaze","2019-01-14",100],
[7,"khaled","2019-01-14",200],[13,"Will","2019-01-15",80],[5,"Elvis","2019-01-15",70],[18,"Jessie","2019-01-16",160],[17,"James","2019-01-16",50],
[44,"Ashley","2019-01-16",140],
[18,"Jessie","2019-01-16",150],[27,"Sakura","2019-01-16",110],[34,"Annabelle","2019-01-16",120]]}}

{"headers": ["VISITED_ON", "amount", "average_amount"], "values": [["2019-01-10", 2940, 420], ["2019-01-11", 3080, 440], ["2019-01-12", 3150, 450],
 ["2019-01-13", 2940, 420], ["2019-01-14", 3780, 540], ["2019-01-15", 3560, 508.57], ["2019-01-16", 3330, 475.71]]}

{"headers": ["visited_on", "amount", "average_amount"], "values": [["2019-01-10", 2940, 420], ["2019-01-11", 3080, 440], ["2019-01-12", 3150, 450],
 ["2019-01-13", 2940, 420.00], ["2019-01-14", 3980, 568.57], ["2019-01-15", 3760, 537.14], ["2019-01-16", 3530, 504.29]]}
