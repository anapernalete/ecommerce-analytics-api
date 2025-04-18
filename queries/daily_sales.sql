SELECT DATE(InvoiceDate) AS SaleDate, SUM(Quantity * UnitPrice) AS TotalRevenue
FROM transactions
WHERE DATE(InvoiceDate) BETWEEN ? AND ?
GROUP BY SaleDate
ORDER BY SaleDate;