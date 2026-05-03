-- Write your query below

with users_in_2020 as (
    select user_id, time_stamp
    from logins l
    where time_stamp > '2020-01-01'
    and time_stamp < '2021-01-01'
)
select user_id, max(time_stamp) as last_stamp
from users_in_2020
group by user_id 
order by last_stamp