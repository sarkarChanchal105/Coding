/*
https://leetcode.com/problems/find-cumulative-salary-of-an-employee/
*/

/*create table employees (Id int, Month int, Salary Int);

insert into employees values(1,1,20);
insert into employees values(2,1,20);
insert into employees values(1,2,30);
insert into employees values(2,2,30);
insert into employees values(3,2,40);
insert into employees values(1,3,40);
insert into employees values(3,3,60);
insert into employees values(1,4,60);
insert into employees values(3,4,70);

*/

--select *, rank() over() from employees

--rename  employees to employee



select * from
(
select 
E1.id , E1.Month 

, NVL(E1.Salary,0)+NVL(E2.Salary,0)+NVL(E3.Salary,0) AS "salary"

from 

employee E1 left join employee E2 on E2.id=E1.id and E2.month=E1.month-1

left join employee E3 on E3.id=E1.id and E3.month=E1.month-2

right join (select id, max(month)max_m from employee  group by id)max_month on E1.id=max_month.id
and E1.month<max_month.max_m

--and E1.id is not null
)A
where id is not null
order by A.id asc, A.month desc



