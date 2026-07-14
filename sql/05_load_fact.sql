-- ==========================================
-- Aggregate Payments
-- ==========================================

WITH payment_summary AS (

    SELECT
        order_id,
        MAX(payment_type) AS payment_type,
        MAX(payment_installments) AS payment_installments,
        SUM(payment_value) AS payment_value
    FROM public.payments
    GROUP BY order_id

)

INSERT INTO warehouse.fact_sales (

    order_id,
    order_item_id,
    customer_id,
    product_id,
    date_id,
    seller_id,
    payment_type,
    payment_installments,
    payment_value,
    review_score,
    price,
    freight_value

)

SELECT

    oi.order_id,
    oi.order_item_id,
    o.customer_id,
    oi.product_id,
    CAST(o.order_purchase_timestamp AS DATE),
    oi.seller_id,
    ps.payment_type,
    ps.payment_installments,
    ps.payment_value,
    r.review_score,
    oi.price,
    oi.freight_value

FROM public.order_items oi

INNER JOIN public.orders o
ON oi.order_id = o.order_id

INNER JOIN warehouse.dim_customer dc
ON o.customer_id = dc.customer_id

INNER JOIN warehouse.dim_product dp
ON oi.product_id = dp.product_id

INNER JOIN warehouse.dim_date dd
ON CAST(o.order_purchase_timestamp AS DATE) = dd.date_id

LEFT JOIN payment_summary ps
ON oi.order_id = ps.order_id

LEFT JOIN public.reviews r
ON oi.order_id = r.order_id;