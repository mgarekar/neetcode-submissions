-- Write your query below

with x as (
    select 
        seat_id,
        free,
        LAG(free) OVER (order by seat_id) as prev_free,
        LEAD(free) OVER (order by seat_id) as next_free       
    from cinema
)
select 
    seat_id
from x
where
    (x.free = 1) and ((x.prev_free = 1) or (x.next_free = 1))