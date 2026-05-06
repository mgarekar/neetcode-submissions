-- Write your query below
with time_in_min as (
    select 
        emp_id,
        event_day,
        (out_time - in_time) as t_event
    from employees
)
select 
    event_day as day,
    emp_id,    
    sum(t_event) as total_time
from time_in_min
group by emp_id,event_day
order by event_day