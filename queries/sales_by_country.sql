SELECT Country, SUM(Quantity * UnitPrice) AS TotalSales
FROM transactions
GROUP BY Country
ORDER BY TotalSales DESC;