-- Write your query below
-- persons = (persons with duplicates) + person without deuplciates

with solo_people as (
    select email
    from person
    group by email
    having count(*) = 1
)
select 
    distinct p.email
from person p
left join solo_people sp
    on p.email= sp.email
where sp.email is NULL