# Zepto Data AI Platform

## Project Overview

This capstone project demonstrates web scraping,
data cleaning, database management, SQL analysis
and pandas-based data processing.

The project is organized into three modules:

1. Data Pipeline
2. Analytics
3. Support Assistant

## Module 1: Data Pipeline

Status: Completed

The data pipeline collects book information
from Books to Scrape.

It performs:
- Web scraping
- Data cleaning
- GBP to INR conversion
- SQLite database creation
- Six SQL queries
- SQL and pandas comparison

Current results:
- 100 books collected
- 29 reported categories
- 100 records inserted into SQLite
- Six SQL queries executed successfully
- SQL JOIN and pandas merge matched

See data_pipeline/README.md for details.

## Module 2: Analytics

Status: To be developed

This module will contain the analytics
component of the capstone.

Implementation details and execution
instructions will be added after development.

## Module 3: Support Assistant

Status: To be developed

This module will contain the support
assistant component of the capstone.

Implementation details and execution
instructions will be added after development.

## Technologies

- Python
- requests
- BeautifulSoup
- pandas
- SQLite

Additional technologies will be documented
as the remaining modules are developed.

## Project Setup

Clone or download the repository.

Open the project folder in VS Code.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Running Module 1

From the project root, run:

```bash
python data_pipeline/main.py
```

This executes the complete data pipeline.

## Running Modules 2 and 3

Instructions will be added when
these modules are implemented.

## Data Source

https://books.toscrape.com/

This website is intended for
web scraping practice.