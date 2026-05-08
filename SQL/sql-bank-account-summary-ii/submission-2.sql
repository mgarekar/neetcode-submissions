-- Write your query below

select 
    u.name,x.balance
    from users u
    join 
    (select 
            account,
            sum(amount) as balance
        from transactions
        group by account
        having sum(amount) > 10000
    ) x
    on x.account = u.account

    -- where u.account IS NOT NULL