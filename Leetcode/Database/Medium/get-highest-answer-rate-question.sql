/*
https://leetcode.com/problems/get-highest-answer-rate-question/
Get the highest answer rate question from a table survey_log with these columns: id, action, question_id, answer_id, q_num, timestamp.

id means user id; action has these kind of values: "show", "answer", "skip"; answer_id is not null when action column is "answer", while is null for "show" and "skip"; q_num is the numeral order of the question in current session.

Write a sql query to identify the question which has the highest answer rate.

Example:

Input:
+------+-----------+--------------+------------+-----------+------------+
| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
Output:
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
Explanation:
question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.
*/


/* Write your PL/SQL query statement below */

select question_id as "survey_log" from
(
select question_id, dense_rank() over(order by ans_rate desc,question_id asc) as rank_
from
(
select
question_id,
sum(case when action='answer' then 1 else 0 end)/
sum(case when action='show' then 1 else 0 end)  as ans_rate
from survey_log
group by question_id
order by 2 desc
)B
)C where rank_=1
--where rownum<2