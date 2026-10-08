-- GOLD: uma linha por item de pedido.
CREATE OR REPLACE TABLE gold_sales AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    p.product_id,
    p.product_name,
    cat.category_id,
    cat.category_name,
    oi.quantity,
    p.price,
    CAST(oi.quantity * p.price AS DECIMAL(12,2)) AS total_amount
FROM silver_orders AS o
INNER JOIN silver_customers AS c ON o.customer_id = c.customer_id
INNER JOIN silver_order_items AS oi ON o.order_id = oi.order_id
INNER JOIN silver_products AS p ON oi.product_id = p.product_id
INNER JOIN silver_categories AS cat ON p.category_id = cat.category_id;
