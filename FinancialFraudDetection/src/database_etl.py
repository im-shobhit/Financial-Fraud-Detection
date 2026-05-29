import sqlite3
import pandas as pd
import os

def run_etl():
    print("Starting ETL Process...")
    
    # Bulletproof path routing (forces Python to find the exact file)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "data", "raw", "credit_card_fraud_dataset.csv")
    db_path = os.path.join(base_dir, "..", "data", "fraud_detection.db")
    
    # Check if data exists
    if not os.path.exists(csv_path):
        print(f"❌ Error: Could not find data file at {csv_path}")
        print("Please verify the file is named 'credit_card_fraud_dataset.csv' exactly.")
        return

    # Extract: Load the raw dataset
    print("Extracting data from CSV...")
    df = pd.read_csv(csv_path)

    # Transform: Clean up column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Load: Connect to SQLite and save the data
    print("Loading data into SQLite Database...")
    conn = sqlite3.connect(db_path)
    
    # Push the dataframe to a SQL table named 'transactions'
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    
    print(f"✅ ETL process completed. Database saved to: {db_path}")

if __name__ == "__main__":
    run_etl()