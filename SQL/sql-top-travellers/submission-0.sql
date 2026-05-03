select 
    u.name,
    coalesce(r.travelled_distance,0) as travelled_distance
from users u
left join 
(
    select 
        user_id,
        sum(distance) as travelled_distance
    from rides
    group by user_id

) r 
on u.id = r.user_id
order by 
    travelled_distance desc,
    u.name asc;