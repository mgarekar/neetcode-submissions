with sold_to_crimson as (
    select o.sales_id as sales_id
    from orders o 
    join company c 
    on o.com_id = c.com_id
    where c.name = 'CRIMSON'
)
select sp.name
    from sales_person sp
    left join sold_to_crimson stc
    on sp.sales_id = stc.sales_id
    where stc.sales_id is null;
