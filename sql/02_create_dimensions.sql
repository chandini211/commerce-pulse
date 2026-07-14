-- ==========================================
-- CUSTOMER DIMENSION
-- ==========================================

CREATE TABLE warehouse.dim_customer (

    customer_id VARCHAR(50) PRIMARY KEY,

    customer_unique_id VARCHAR(50),

    customer_zip_code_prefix INT,

    customer_city VARCHAR(100),

    customer_state CHAR(2)

);

-- ==========================================
-- PRODUCT DIMENSION
-- ==========================================

CREATE TABLE warehouse.dim_product (

    product_id VARCHAR(50) PRIMARY KEY,

    product_category_name VARCHAR(100),

    product_name_lenght INT,

    product_description_lenght INT,

    product_photos_qty INT,

    product_weight_g INT,

    product_length_cm INT,

    product_height_cm INT,

    product_width_cm INT

);

-- ==========================================
-- DATE DIMENSION
-- ==========================================

CREATE TABLE warehouse.dim_date (

    date_id DATE PRIMARY KEY,

    day INT,

    month INT,

    quarter INT,

    year INT,

    day_of_week INT,

    month_name VARCHAR(20)

);