select * from
(select eid,ename,sal,job,locationn,dense_rank() over(partition by id) as rn from empy
where rn = 3) empy;