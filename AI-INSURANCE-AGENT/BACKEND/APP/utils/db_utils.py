import sqlite3

def get_all_plans():
    # Connect to DB
    conn = sqlite3.connect("data/insurance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM insurance_plans")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_plans():
    # Sample insurance plans
    return [
        {"name": "Plan A", "type": "Health", "premium": 5000},
        {"name": "Plan B", "type": "Life", "premium": 3000}
    ]
