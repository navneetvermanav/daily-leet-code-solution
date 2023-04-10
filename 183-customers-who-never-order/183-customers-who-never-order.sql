# Write your MySQL query statement below
SELECT name AS Customers FROM Customers A WHERE NOT EXISTS (SELECT * FROM Orders B WHERE A.id = B.customerId);
