-- Write your query below

select c.name
from customers c  left join orders o on c.id = o.customer_id
where o.id is NULL;

--c.id, c.name, o.customer_id, o.id