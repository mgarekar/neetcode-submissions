-- Write your query below
select 
    distinct c.title

from tv_program tv
    join content c
    on tv.content_id = c.content_id

where
    date(tv.program_date) >= date '2020-06-01'
    and date (tv.program_date) <= date '2020-06-30'
    and c.kids_content = 'Y'
    and c.content_type = 'Movies'