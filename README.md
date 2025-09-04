Customer Epic — Plan smarter, greener trips

Goal: Help customers quickly find and compare flights by destination, dates, time, price, and impact.

Story C1 — Filter by destination & dates with KPIs

As a customer, I want to filter flights by destination country and a date range (Apr–Aug 2022) so I only see relevant options with quick indicators of price and duration.

Acceptance Criteria

Given the Overview page
When I choose a destination country and date range within Apr–Aug 2022
Then the table shows only matching flights
And KPIs display Avg Price (USD) and Median Duration (hrs) for the filtered set
And the destination bar chart reflects the same filters.

Story C2 — Compare two destinations

As a customer, I want to compare two destination countries to see arrival timelines, the highest/lowest prices (with airline), and flight durations.

Acceptance Criteria

Given the Compare Countries page
When I select Country A and Country B and set a date range
Then I see a timeline of arrivals (date & time) by country
And KPIs for Highest/Lowest price with airline for each country
And a duration distribution chart (boxplot + points).

Environmental Data Analyst Epic — Quantify emissions drivers

Goal: Identify aircraft and patterns that contribute most to CO₂ and ensure data quality for analysis.

Story A1 — Standardise & enrich dataset

As an environmental data analyst, I want to standardise and enrich the CSV (units, datetimes, derived fields) so it’s analysis-ready for loading to PostgreSQL.

Acceptance Criteria

Given the raw CSV
When the transform step runs
Then durations are converted to hours, CO₂ to kg, stops → is_direct, price normalised (if needed), and datetimes parsed
And column names are consistent (snake_case) with missing/duplicate handling documented.

Story A2 — Rank aircraft by average CO₂

As an environmental data analyst, I want a leaderboard of aircraft types by average CO₂ per flight (kg) to identify high emitters.

Acceptance Criteria

Given aircraft_type and emissions columns
When I open the CO₂ view and choose a Top-N
Then emissions are normalised to kg, aggregated by aircraft_type, sorted descending, and displayed as a bar chart with tooltips.

Business Owner Epic — Monitor market & sustainability KPIs

Goal: Track demand, pricing, and emissions to guide commercial and sustainability decisions.

Story B1 — Top destinations & direct/connecting mix (Apr–Aug)

As a business owner, I want a Top destinations chart (Apr–Aug 2022) and a KPI for the share of direct flights to understand demand and product mix.

Acceptance Criteria

Given the Overview page
When the month filter covers Apr–Aug 2022
Then I see the Top 10 destination countries by flight count
And KPIs for Unique Routes and Direct flights (count or % where stops == 0).

Story B2 — Pricing outliers by destination

As a business owner, I want to see the highest and lowest prices per destination (with airline) to spot outliers and opportunities.

Acceptance Criteria

Given the destination comparison view
When I select any destination and date range
Then I see Highest and Lowest price entries with airline names
And I can expand to view underlying flight details (date/time, airline, duration).

Definition of Done (applies to all stories)

Units are explicit (USD, hours, kg CO₂); charts & KPIs reflect filters consistently.

Empty states handled (e.g., “No data for selection”).

CSV export (if offered) matches the current filters.

Typical interactions respond in ~≤2 seconds for ≤10k rows.

No secrets committed: credentials in .env / .streamlit/secrets.toml only.
