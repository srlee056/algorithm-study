SELECT p.PRODUCT_CODE,
    SUM(p.price*os.sales_amount) as SALES
from PRODUCT p
JOIN OFFLINE_SALE os
ON p.PRODUCT_ID = os.PRODUCT_ID
group by p.PRODUCT_CODE
ORDER BY SALES desc, p.PRODUCT_CODE