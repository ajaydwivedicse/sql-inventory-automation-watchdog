import mysql.connector
from datetime import datetime


def run_inventory_watchdog():
    print(f" SQL Watchdog Active... [{datetime.now().strftime('%Y-%m-%d %H:%M')}]")

    try:
        # 1. Update these credentials for your local MySQL
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "root",
            "database": "grocery_db"
        }

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # 2. Advanced Query: Select items where stock is less than their specific threshold
        query = "SELECT product_name, current_stock, min_threshold FROM inventory WHERE current_stock < min_threshold"

        cursor.execute(query)
        alerts = cursor.fetchall()

        # 3. Output the results
        if alerts:
            print("\n [SYSTEM ALERT] INVENTORY CRITICAL")
            print("=" * 45)
            for item in alerts:
                print(
                    f" {item['product_name']}: {item['current_stock']} units left (Threshold: {item['min_threshold']})")
            print("=" * 45)
            print("Action: Please restock immediately.")
        else:
            print(" Status: All stock levels are sufficient.")

    except mysql.connector.Error as e:
        print(f" Connection Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    run_inventory_watchdog()