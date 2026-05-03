# SQL Inventory Automation Watchdog

This project is a backend automation solution that monitors a MySQL database and triggers critical alerts when stock levels fall below a specific threshold. It bridges the gap between database management and real-time business operations.

## Problem Solved
Manually checking inventory in a database is time-consuming and prone to human error. This tool automates the process, ensuring that "Out of Stock" scenarios are avoided by alerting management the moment a product hits its minimum threshold.

## Tech Stack
* **Language:** Python 3.x
* **Database:** MySQL
* **Libraries:** `mysql-connector-python`
* **Logic:** Relational Data Comparison

## Key Features
* **Threshold-Based Alerts:** Dynamically compares `current_stock` against `min_threshold` stored in the database.
* **Database Integration:** Demonstrates secure Python-to-MySQL connectivity.
* **Actionable Logging:** Generates clear, timestamped alerts for immediate restock actions.

## How to Set Up
1. **Database Setup:** 
   - Open MySQL Workbench.
   - Run the provided `setup_inventory.sql` to create the database and sample data.
2. **Installation:**
   - Install the connector: `pip install mysql-connector-python`
3. **Configuration:**
   - Update the `db_config` in `watchdog.py` with your local MySQL password.
4. **Run:**
   - `python watchdog.py`

## Business Logic Demo
If the database contains:
- `Red Apples`: 4 units (Threshold: 15)
- `Fresh Milk`: 25 units (Threshold: 10)

**The Watchdog will output:**
`[SYSTEM ALERT] INVENTORY CRITICAL: Red Apples (4 units left)`
