
sql query to find the average salary of emoloyees by dept by excludingg top 10% earners employee_salary table has columns like emp_id,dept_id,salary and table dept_salary has columns dept_id,average_salary

select 

copy file
gsutil cp -m c:drive/file.csv  gs://bukcet_name
gsutil mv  c:drive.file gs://bukcet_name
gsutil ls
gsutil rm gs://bukcet_name

select id, cast(id as string) as id_sting from table_nae

top 3 players who scored max goals?

with cte as (
select players,goals,row_number() over(paritiotn by season order by goals desc) as rank in games)

select players,goals from cte where rank <=3;


