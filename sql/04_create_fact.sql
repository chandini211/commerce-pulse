-- ==========================================
-- FACT SALES TABLE
-- ==========================================

CREATE TABLE warehouse.fact_sales (

    sales_key SERIAL PRIMARY KEY,

    order_id VARCHAR(50),

    order_item_id INT,

    customer_id VARCHAR(50),

    product_id VARCHAR(50),

    date_id DATE,

    seller_id VARCHAR(50),

    payment_type VARCHAR(30),

    payment_installments INT,

    payment_value NUMERIC(10,2),

    review_score INT,

    price NUMERIC(10,2),

    freight_value NUMERIC(10,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES warehouse.dim_customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES warehouse.dim_product(product_id),

    CONSTRAINT fk_date
        FOREIGN KEY (date_id)
        REFERENCES warehouse.dim_date(date_id)

);