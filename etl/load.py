
import os
import pandas as pd
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv


def main():
    load_dotenv()

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(connection_url)

    data_path = "data/processed"

    files = {
        "customers": "customers.csv",
        "orders": "orders.csv",
        "order_items": "order_items.csv",
        "products": "products.csv",
        "payments": "payments.csv",
        "reviews": "reviews.csv"
    }

    for table_name, file_name in files.items():
        print(f"\nLoading {table_name}...")

        df = pd.read_csv(f"{data_path}/{file_name}")

        df.to_sql(
            name=table_name,
            con=engine,
            schema="public",
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded: {len(df)} rows")

    engine.dispose()
    print("\nAll tables loaded successfully!")


if __name__ == "__main__":
    main()
