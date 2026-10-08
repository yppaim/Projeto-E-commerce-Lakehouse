-- SILVER: limpeza, padronização e tipagem.
CREATE OR REPLACE TABLE silver_customers AS
SELECT
    CAST(customer_id AS INTEGER) AS customer_id,
    NULLIF(TRIM(name), '') AS customer_name,
    NULLIF(TRIM(city), '') AS city,
    UPPER(NULLIF(TRIM(state), '')) AS state
FROM bronze_customers;

CREATE OR REPLACE TABLE silver_categories AS
SELECT
    CAST(category_id AS INTEGER) AS category_id,
    NULLIF(TRIM(category_name), '') AS category_name
FROM bronze_categories;

CREATE OR REPLACE TABLE silver_products AS
SELECT
    CAST(product_id AS INTEGER) AS product_id,
    NULLIF(TRIM(product_name), '') AS product_name,
    CAST(price AS DECIMAL(10,2)) AS price,
    CAST(category_id AS INTEGER) AS category_id
FROM bronze_products;

CREATE OR REPLACE TABLE silver_orders AS
SELECT
    CAST(order_id AS INTEGER) AS order_id,
    CAST(customer_id AS INTEGER) AS customer_id,
    CAST(order_date AS DATE) AS order_date
FROM bronze_orders;

CREATE OR REPLACE TABLE silver_order_items AS
SELECT
    CAST(order_id AS INTEGER) AS order_id,
    CAST(product_id AS INTEGER) AS product_id,
    CAST(quantity AS INTEGER) AS quantity
FROM bronze_order_items;
