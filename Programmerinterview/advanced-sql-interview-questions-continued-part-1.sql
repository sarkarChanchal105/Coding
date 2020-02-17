/*
 https://www.programmerinterview.com/database-sql/advanced-sql-interview-questions-and-answers/
*/

create table salesperson (ID number, Name VARCHAR2(10), Age Number,Salary Number);

create table orders ("Number" Number, order_date date, cust_id number,salesperson_id number, Amount number);

insert into salesperson values(1,'Abe',61,140000);
insert into salesperson values(2,'Bob',34,44000);
insert into salesperson values(5,'Chris',34,40000);
insert into salesperson values(7,'Dan',41,52000);
insert into salesperson values(8,'Ken',57,115000);
insert into salesperson values(11,'Joe',38,38000);

commit;

insert into orders values(10,to_date('8/2/96','mm/dd/yy'),4,2,540);

insert into orders values(20,to_date('1/30/99','mm/dd/yy'),4,8,1800);
insert into orders values(30,to_date('7/14/95','mm/dd/yy'),9,1,460);
insert into orders values(40,to_date('1/29/98','mm/dd/yy'),7,2,2400);
insert into orders values(50,to_date('2/3/98','mm/dd/yy'),6,7,600);
insert into orders values(60,to_date('3/2/98','mm/dd/yy'),6,7,720);
insert into orders values(70,to_date('5/6/98','mm/dd/yy'),9,7,150);

COMMIT;



SELECT s.name FROM salesperson S JOIN orders O ON o.salesperson_id=s.id
group by s.name
having count(s.name)>1;




create table Starbucks_Employees(id number, Name varchar2(100),Age Number,HourlyRate Number,StoreID Number);

create table Starbucks_Stores(store_id number, city varchar2(100));

insert into Starbucks_Employees values(1,'Abe',61,14,10);
insert into Starbucks_Employees values(2,'Bob',34,10,30);
insert into Starbucks_Employees values(5,'Chris',34,9,40);
insert into Starbucks_Employees values(7,'Dan',41,11,50);
insert into Starbucks_Employees values(8,'Ken',57,11,60);
insert into Starbucks_Employees values(11,'Joe',38,13,70);
