--select * from tab;

create table hierarchy_raw (hier varchar2(500));

insert into hierarchy_raw values('grand1,father1,child1');

select * from hierarchy_raw;

select 
hier
, substr(hier,1,instr(hier,',',1)-1) as grandfather 
, substr(hier,instr(hier,',',1)+1,instr(hier,',',2)) as father 
, instr(hier,',',2) 
,length(hier)
from hierarchy_raw;

select hier

,substr(hier,1,instr(hier,',',1,1)-1) as grandfather  
,substr(hier,instr(hier,',',1,1)+1,(instr(hier,',',1,2)-instr(hier,',',1,1))-1) as father
,substr(hier,instr(hier,',',1,2)+1,(length(hier) -instr(hier,',',1,2))-1) as child
from hierarchy_raw

--instr(hier,',',1,1), instr(hier,',',1,2),  from hierarchy_raw;



