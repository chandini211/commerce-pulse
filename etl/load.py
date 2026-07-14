import os

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


def main():

    # -----------------------------
    # Load Environment Variables
    # -----------------------------
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # -----------------------------
    # Database Connection
    # -----------------------------
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # -----------------------------
    # Processed Data Path
    # -----------------------------
    DATA_PATH = "data/processed"

    files = {
        "customers": "customers.csv",
        "orders": "orders.csv",
        "order_items": "order_items.csv",
        "products": "products.csv",
        "payments": "payments.csv",
        "reviews": "reviews.csv"
    }

    # -----------------------------
    # Load CSV Files into PostgreSQL
    # -----------------------------
    for table_name, file_name in files.items():

        print(f"\nLoading {table_name}...")

        df = pd.read_csv(f"{DATA_PATH}/{file_name}")

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} Loaded Successfully")
        print(f"Rows Loaded: {len(df)}")

    print("\nAll Tables Loaded Successfully!")


if __name__ == "__main__":
    main()