-- ==========================================================
-- LOAD CUSTOMER DIMENSION
-- ==========================================================

INSERT INTO warehouse.dim_customer
(
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
)
SELECT
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
FROM public.customers;


-- ==========================================================
-- LOAD PRODUCT DIMENSION
-- ==========================================================

INSERT INTO warehouse.dim_product
(
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
SELECT
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
FROM public.products;


-- ==========================================================
-- LOAD DATE DIMENSION
-- ==========================================================

INSERT INTO warehouse.dim_date
(
    date_id,
    day,
    month,
    quarter,
    year,
    day_of_week,
    month_name
)

SELECT DISTINCT

DATE(order_purchase_timestamp) AS date_id,

EXTRACT(DAY FROM CAST(order_purchase_timestamp AS TIMESTAMP)),

EXTRACT(MONTH FROM CAST(order_purchase_timestamp AS TIMESTAMP)),

EXTRACT(QUARTER FROM CAST(order_purchase_timestamp AS TIMESTAMP)),

EXTRACT(YEAR FROM CAST(order_purchase_timestamp AS TIMESTAMP)),

EXTRACT(DOW FROM CAST(order_purchase_timestamp AS TIMESTAMP)),

TO_CHAR(CAST(order_purchase_timestamp AS TIMESTAMP),'Month')

FROM public.orders

WHERE order_purchase_timestamp IS NOT NULL;