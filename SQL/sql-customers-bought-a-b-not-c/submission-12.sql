-- no C


select o.customer_id, c.customer_name 
From
    ( 
        select customer_id
        from orders
        group by customer_id
        having (
            SUM( 
                case 
                    when (product_name = 'A') then 1
                    else 0 
                end
            ) > 0 and
            SUM( 
                case 
                    when (product_name = 'B') then 1
                    else 0 
                end
            ) > 0 and
            SUM( 
                case 
                    when (product_name = 'C') then 1
                    else 0 
                end
            ) = 0
        )
    ) o

    left join customers c 

on o.customer_id = c.customer_id
order by c.customer_name;
------------
-- C haters, but A & B buyers

