import pandas as pd
from pathlib import Path


def main():

    # -----------------------------
    # Paths
    # -----------------------------
    RAW_PATH = Path("data/raw")
    PROCESSED_PATH = Path("data/processed")
    PROCESSED_PATH.mkdir(exist_ok=True)

    # -----------------------------
    # Load Data
    # -----------------------------
    customers = pd.read_csv(RAW_PATH / "customers.csv")
    orders = pd.read_csv(RAW_PATH / "orders.csv")
    order_items = pd.read_csv(RAW_PATH / "order_items.csv")
    payments = pd.read_csv(RAW_PATH / "order_payments.csv")
    reviews = pd.read_csv(RAW_PATH / "order_reviews.csv")
    products = pd.read_csv(RAW_PATH / "products.csv")
    sellers = pd.read_csv(RAW_PATH / "sellers.csv")
    geolocation = pd.read_csv(RAW_PATH / "geolocation.csv")
    category = pd.read_csv(RAW_PATH / "product_category_name_translation.csv")

    # -----------------------------
    # Convert Date Columns
    # -----------------------------
    date_columns = {
        "orders": [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ],
        "order_items": [
            "shipping_limit_date"
        ],
        "reviews": [
            "review_creation_date",
            "review_answer_timestamp"
        ]
    }

    for col in date_columns["orders"]:
        orders[col] = pd.to_datetime(orders[col])

    for col in date_columns["order_items"]:
        order_items[col] = pd.to_datetime(order_items[col])

    for col in date_columns["reviews"]:
        reviews[col] = pd.to_datetime(reviews[col])

    # -----------------------------
    # Data Cleaning
    # -----------------------------
    geolocation = geolocation.drop_duplicates()

    products = products.dropna(
        subset=[
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
    )

    # -----------------------------
    # Feature Engineering
    # -----------------------------
    orders["delivery_days"] = (
        orders["order_delivered_customer_date"] -
        orders["order_purchase_timestamp"]
    ).dt.days

    orders["approval_days"] = (
        orders["order_approved_at"] -
        orders["order_purchase_timestamp"]
    ).dt.days

    orders["purchase_year"] = (
        orders["order_purchase_timestamp"]
        .dt.year
    )

    orders["purchase_month"] = (
        orders["order_purchase_timestamp"]
        .dt.month
    )

    orders["purchase_month_name"] = (
        orders["order_purchase_timestamp"]
        .dt.month_name()
    )

    # -----------------------------
    # Save Processed Data
    # -----------------------------
    datasets = {
        "customers": customers,
        "orders": orders,
        "order_items": order_items,
        "payments": payments,
        "reviews": reviews,
        "products": products,
        "sellers": sellers,
        "geolocation": geolocation,
        "category": category
    }

    for name, df in datasets.items():
        df.to_csv(PROCESSED_PATH / f"{name}.csv", index=False)

    print("ETL Transformation Completed Successfully!")


if __name__ == "__main__":
    main()