-- SELECT DISTINCT(Destination) FROM indigo.flights_data
-- UNION
-- SELECT DISTINCT(Source) FROM indigo.flights_data


-- SELECT * FROM indigo.flights_data
-- WHERE Source = 'Banglore' AND Destination = 'Delhi'


-- SELECT Airline, COUNT(*) FROM indigo.flights_data
-- GROUP BY Airline


-- SELECT Source, COUNT(*) FROM (SELECT Source FROM indigo.flights_data
-- 				UNION ALL
-- 				SELECT Destination FROM indigo.flights_data) t
-- GROUP BY t.Source
-- ORDER BY COUNT(*) DESC 

SELECT Date_of_Journey, COUNT(*) FROM indigo.flights_data
GROUP BY Date_of_Journey