-- 코드를 입력하세요
SELECT * from PLACES
WHERE HOST_ID in
(SELECT HOST_ID
from PLACES
group by HOST_ID 
HAVING count(*) >= 2)
order by ID asc;