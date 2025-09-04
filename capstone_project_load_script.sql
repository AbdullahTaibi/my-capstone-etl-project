SELECT * FROM abdullah_etl_capstone_project;

SELECT COUNT(DISTINCT dest_country) AS unique_country_count
FROM abdullah_etl_capstone_project;

SELECT 
  dest_country,
  COUNT(*) AS visit_count,
  RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
FROM abdullah_etl_capstone_project
GROUP BY dest_country
ORDER BY rank;

SELECT * FROM abdullah_etl_capstone_project;

SELECT DISTINCT UNNEST(string_to_array(aircraft_type, '|')) AS aircraft
FROM abdullah_etl_capstone_project;

SELECT dest_country, COUNT(*) AS flight_count
FROM (
    SELECT dest_country, UNNEST(string_to_array(aircraft_type, '|')) AS aircraft
    FROM abdullah_etl_capstone_project
) AS expanded
WHERE aircraft = 'Airbus A321neo'
GROUP BY dest_country
ORDER BY flight_count DESC;

SELECT 
    dest_country,
    COUNT(*) AS flight_count,
    SUM(co2_emissions) AS total_emissions,
    AVG(co2_emissions) AS avg_emissions
FROM (
    SELECT dest_country, co2_emissions, UNNEST(string_to_array(aircraft_type, '|')) AS aircraft
    FROM abdullah_etl_capstone_project
) AS expanded
WHERE aircraft = 'Airbus A321neo'
GROUP BY dest_country
ORDER BY total_emissions DESC;

SELECT airline_name, COUNT(*) AS flight_count
FROM abdullah_etl_capstone_project
GROUP BY airline_name
ORDER BY flight_count DESC
LIMIT 40;
