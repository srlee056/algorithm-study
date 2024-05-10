SELECT ii.ITEM_ID,
    ii.ITEM_NAME
    FROM ITEM_INFO ii
    LEFT JOIN ITEM_TREE it
    ON ii.ITEM_ID = it.ITEM_ID
    where PARENT_ITEM_ID IS NULL
    order by ii.ITEM_ID;