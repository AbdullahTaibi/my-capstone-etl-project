# Flights Capstone Project

![Curiosidades sobre viajar en avión](https://www.grupooneair.com/wp-content/uploads/2023/06/10-cuirosidades-sobre-viajar-en-avion.jpg)




# Project Overview

Flights are considered a luxury good in economical concepts, meaning as your income increases you would increase your consumption of such transport method. When booking a flight, or a number of flights, it is important to consider several factors, including season, necessity, type of plane, ticket prices, and ultimately how long the flights take due to different routes airlines prefer to take as part of their journey. The analysis made from this project will show two visualisations of metrics compared of flight data between April to August of 2022.

Project purpose

The goal is to analyse worldwide flights to understand patterns in flight duration, CO₂ emissions, stops, and price, and to surface meaningful trends.
The dataset is a CSV containing flight details across countries: airlines, dates, durations, stops, and additional measurable attributes. The workflow:

- Extract the CSV
- Transform and standardise with Pandas
- Load into PostgreSQL (DBeaver used as the SQL client)
- Visualise insights with Streamlit

Tech stack

- Python — environment & orchestration
- Pandas — data cleaning, standardisation, enrichment
- PostgreSQL — storage & analysis (queried via DBeaver)
- Streamlit — interactive application & visualisations

## Epic 1

As a Environment Data Analyst, I want to extract the Flights data from the CSV file, so that I can enrich the data accordingly.

### User Story 1

As a Data Analyst, I want to extract the CSV file using Pandas so that I can transform and compile this for further analysis.

## Epic 2

As a Environment Data Analyst, I want to standardise, enrich, clean, convert the data, so that it is ready to be used when ready to load.

### User 2

As a Environment Data Analyst, I want to clean, remove, add, and separate columns to have consistency and better readability.

### User 3

As a Environment Data Analyst, I want to remove duplicates, rows with any missing value(s), so that the analysis can be conducted with margin for errors.

## Epic 3

As a Environment Data Analyst, I want to run the ETL pipeline to simultaneously run my VS Code with the PostgreSQL database, so that analysis on flight metrics can be measured.

### User 4

As a Environment Data Analyst, I want to store the transformed CSF file, cleaned and readily available as a single table in PostgreSQL, so that queries can be written to one table only.

## Epic 4

As a Data Analyst, I want to gain insights and rends in the data, so that I can draw relevant conclusions that highlight trends and help take further actions.

### User 5
As a Business owner, I want to see the data on pricing, flexibility of airlines, so that I can depict what can be done to enhance flexibility of routes to take.

### User 6
As a customer, I want to be able to see the price of flights, how long flights are, and how many stops are on this journey, so that I can make better decisions for when I travel.
