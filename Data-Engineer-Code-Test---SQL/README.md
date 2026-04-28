# Data-Engineer-Code-Test---SQL
#Test for SQL
WITH LatestRedemptions AS (
    SELECT 
        retailerId, 
        redemptionDate, 
        redemptionCount, 
        createDateTime,
        ROW_NUMBER() OVER (PARTITION BY retailerId, redemptionDate ORDER BY createDateTime DESC) AS rn
    FROM 
        `my_project.my_dataset.tblRedemptions-ByDay`
    WHERE
        retailerId = (SELECT id FROM `my_project.my_dataset.tblRetailers` WHERE retailerName = 'ABC Store')
        AND redemptionDate BETWEEN '2023-10-30' AND '2023-11-05'
)
SELECT 
    redemptionDate, 
    redemptionCount 
FROM 
    LatestRedemptions
WHERE 
    rn = 1
ORDER BY 
    redemptionDate;
