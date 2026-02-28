# CSV Customer Transformation ETL Pipeline

## 📌 Project Overview

This project is a **Python-based ETL (Extract, Transform, Load) pipeline** designed to process a CSV dataset containing **10,000 customer records**. The pipeline demonstrates fundamental data engineering pipeline development by performing data extraction, transformation, and loading operations.

The pipeline follows a modular design approach to maintain clean architecture and code reusability.


## 📂 Project Structure
DE Project 1/
│
├── Data/
│ └── customers-10000.csv
│
├── extract_data.py
│ - Responsible for reading and extracting data from CSV dataset
│
├── data_transformation.py
│ - Performs data cleaning and multiple transformation operations such as:
│ - Handling missing values
│ - Removing duplicate records
│ - Data type conversions
│ - Dataset standardization
│
├── postgres_loader.py
│ - Creates PostgreSQL table schema
│ - Loads transformed data into PostgreSQL database
│
├── main.py
│ - Executes the complete ETL pipeline by calling extraction, transformation, and loading modules
│
├── .env
│ - Stores database credentials securely
│
├── .gitignore
│ - Prevents sensitive and unnecessary files from being pushed to GitHub
│
└── venv/
└── Python virtual environment



## ⚙️ ETL Pipeline Workflow

### 1. Extraction Phase
- Reads customer dataset from CSV file using **Pandas**
- Loads raw data into memory for processing

### 2. Transformation Phase
The transformation module performs various data preprocessing operations including:

- Replacing invalid or missing values  
- Dropping duplicate records  
- Converting columns to appropriate data types  
- Cleaning inconsistent dataset entries  

### 3. Loading Phase
- Establishes connection with **PostgreSQL database**
- Creates table schema for customer data storage
- Inserts transformed dataset into database tables


## 🛠️ Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy / Psycopg2 (depending on implementation)
- dotenv (for environment variable management)

---
