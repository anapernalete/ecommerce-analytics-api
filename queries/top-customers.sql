SELECT CustomerID, SUM(Quantity * UnitPrice) AS TotalSpent
FROM transactions
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 10;