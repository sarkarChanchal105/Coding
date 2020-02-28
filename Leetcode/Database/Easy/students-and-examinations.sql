/*
https://leetcode.com/problems/students-and-examinations/


Create table Students (student_id int, student_name varchar(20));
Create table  Subjects (subject_name varchar(20));
Create table  Examinations (student_id int, subject_name varchar(20));

Truncate table Students;
insert into Students (student_id, student_name) values ('1', 'Alice');
insert into Students (student_id, student_name) values ('2', 'Bob');
insert into Students (student_id, student_name) values ('13', 'John');
insert into Students (student_id, student_name) values ('6', 'Alex');
Truncate table Subjects;
insert into Subjects (subject_name) values ('Math');
insert into Subjects (subject_name) values ('Physics');
insert into Subjects (subject_name) values ('Programming');
Truncate table Examinations;
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Programming');
insert into Examinations (student_id, subject_name) values ('2', 'Programming');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Programming');
insert into Examinations (student_id, subject_name) values ('13', 'Physics');
insert into Examinations (student_id, subject_name) values ('2', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Math');

commit;


*/

/* uses corelated sub query

for each row in the outer query the inner qeuery is evaluated.

*/

SELECT
    student_id,
    student_name,
    subject_name,
    (
        SELECT count(*) FROM Examinations  e
        WHERE e.student_id = Students.student_id
        AND e.subject_name = Subjects.subject_name
    ) AS attended_exams
FROM Students, Subjects
ORDER BY student_id ASC, subject_name ASC;









