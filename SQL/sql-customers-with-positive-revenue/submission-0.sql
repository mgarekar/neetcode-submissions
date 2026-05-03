
select customer_id 
from
    ( select customer_id, sum(revenue) as total_revenue
    from customers
    where year = 2020
    group by customer_id     ) as t
where total_revenue > 0;