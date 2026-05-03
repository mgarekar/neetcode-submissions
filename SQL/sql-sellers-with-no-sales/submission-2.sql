-- Write your query below

with orders_seller as (
    select 
        s.seller_id as seller_id,
        s.seller_name as seller_name,        
        o.order_id as order_id,
        o.sale_date as sale_date 
    from orders o 
    right join seller s
    on o.seller_id = s.seller_id
    and o.sale_date >= '2020-01-01'
    and o.sale_date < '2021-01-01'
)
select seller_name 
from orders_seller
where 
    order_id is null
order by seller_name