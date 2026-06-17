# ⚽ Football Intelligence & Transfer Analytics Platform (FITAP)

## Overview

FITAP is an end-to-end Data Engineering project that collects, processes, transforms, and analyzes football player and team performance data. The platform enables player scouting, team performance analysis, and football intelligence reporting using modern cloud-based data engineering tools.

## Architecture

```text
API-Football
     │
     ▼
Python ETL
     │
     ▼
AWS S3
     │
     ▼
Snowflake
(Bronze → Silver → Gold)
     │
     ▼
dbt
     │
     ▼
Power BI
```

## Tech Stack

- Python
- AWS S3
- Snowflake
- dbt
- Power BI
- Git & GitHub

## Data Sources

Data is collected from API-Football (API-Sports), covering:

- Premier League
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- Eredivisie
- MLS
- Saudi Pro League
- Portuguese Liga

## Key Features

- Automated football data extraction using Python
- Cloud storage using AWS S3
- Snowflake-based Medallion Architecture
- dbt staging, dimension, and fact models
- Data quality testing using dbt
- Player and team performance analytics
- Transfer scouting and ranking metrics

## Data Models

### Dimensions

- dim_players
- dim_teams

### Facts

- fact_player_performance
- fact_team_performance
- fact_player_rankings

## Business Insights

- Top Goal Scorers
- Top Assist Providers
- Team Performance Rankings
- Player Efficiency Analysis
- Goal Conversion Analysis
- Transfer Scouting Support

## Future Enhancements

- Apache Airflow orchestration
- Automated pipeline scheduling
- Live football match ingestion
- FIFA World Cup analytics
- CI/CD with GitHub Actions
- Advanced Power BI dashboards

## Author

**Rohit Uniyal**

Data Engineering Portfolio Project
