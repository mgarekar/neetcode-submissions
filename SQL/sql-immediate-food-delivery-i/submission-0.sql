-- Write your query below

with immediate_added as (
    select 
        *,
        case 
            when (order_date=customer_pref_delivery_date) then 1
            else 0
        end as immediate
    from delivery
)
select 
       ROUND(
            ( SUM(immediate) * 100.0 / COUNT(*))
            ,2
       ) as immediate_percentage
from immediate_added