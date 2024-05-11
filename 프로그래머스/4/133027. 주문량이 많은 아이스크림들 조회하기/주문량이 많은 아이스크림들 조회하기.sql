select first_half.FLAVOR
from FIRST_HALF first_half
JOIN 
(
select FLAVOR, SUM(TOTAL_ORDER) as TOTAL_ORDER
from JULY
group by FLAVOR) july
ON first_half.FLAVOR = july.FLAVOR
order by (first_half.TOTAL_ORDER + july.TOTAL_ORDER) desc
LIMIT 3;


