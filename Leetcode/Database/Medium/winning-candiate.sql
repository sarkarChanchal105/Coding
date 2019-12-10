/*
https://leetcode.com/problems/winning-candidate/
*/

/* Write your PL/SQL query statement below */

select name from
(
select name, count_ ---, rank() over(order by count_ desc,name desc ) as rank_
from
(
select candidate.name, count(vote.id) count_

from vote join candidate on vote.candidateId=candidate.id

group by candidate.name
)A
order by count_ desc
) B
where rownum<2

