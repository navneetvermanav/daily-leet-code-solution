# Write your MySQL query statement below
Select Firstname , lastname ,city , state from person as p left join address as a on p.personId = a.personId
