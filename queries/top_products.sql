SELECT Description, SUM(Quantity) AS TotalSold
FROM transactions
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT ?;