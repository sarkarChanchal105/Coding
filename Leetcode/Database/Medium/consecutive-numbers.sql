/*

https://leetcode.com/problems/consecutive-numbers/
*/

SELECT DISTINCT L1.Num ConsecutiveNums

FROM Logs L1 join Logs L2 on L1.Id+1=L2.Id
join Logs L3 on L2.Id+1=L3.Id
where L1.Num=L2.Num
and L2.Num=L3.Num