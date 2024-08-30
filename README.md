# Data_ETL_Project

## Overview

Welcome to the Data_ETL_Project repository. This project showcases the end-to-end process of Extracting, Transforming, and Loading (ETL) data, followed by comprehensive analysis and visualization. Leveraging Python and PostgreSQL, this project transforms raw data into actionable insights.

## Project Context

This project simulates a real-world ETL scenario, offering practical experience in data manipulation and visualization. The dataset, initially in CSV format, represents candidate performance data. The goal was to transfer this data into a cleaned relational database and create meaningful visualizations to represent various metrics through a dashboard.

Key aspects of the project include:

- Migrating candidate data into a PostgreSQL database.
- Utilizing Python and Jupyter Notebook for data handling and analysis, and storing data in PostgreSQL database for efficient management.
- Generating visualizations for metrics such as technology distribution, annual hires, seniority levels, and hires by countries like the USA, Brazil, Colombia, and Ecuador.


To qualify as "hired," candidates needed to score at least 7 in both the coding challenge and the technical interview.

## Technologies

The necesary tools for this proyect are:

- Python
- Jupyter Notebook
- PostgreSQL
- Power BI

## Dashboard

The project includes a dashboard made by PowerBi that visualizes:

- Hires by technology
- Annual hiring trends
- hires by Seniority level
- Hires by Country focusing on specific countries

![Dashboard](data-README.md\DashboardScreenshot.png)

## Getting Started

### Setup the Environment:

1. Install PostgreSQL
2. Create a virtual environment and install the dependencies listed in requirements.txt.
3. Configure the connection to the PostgreSQL database. I recommend the creation of a .env file with the credentials and check the scripts to edit the new routes.

### Data Preparation

**Run** `migration.py` and `EDA.ipynb` to clean and migrate data.

### Data Visualization

**Connect** Power BI to the PostgreSQL DB to create the dashboard required in the challenge.

### Scripts:

- `migration.py`: Migrates data from CSV to PostgreSQL.
- `EDA.ipynb`: Clean and analyzes data.


Feel free to explore the repository and adapt the scripts to suit your needs!