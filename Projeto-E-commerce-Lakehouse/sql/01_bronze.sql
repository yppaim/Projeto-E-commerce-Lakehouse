-- BRONZE: ingestão dos CSVs RAW preservando a estrutura de origem.
CREATE OR REPLACE TABLE bronze_customers AS
SELECT * FROM read_csv_auto('data/raw/customers.csv', header = true);

CREATE OR REPLACE TABLE bronze_categories AS
SELECT * FROM read_csv_auto('data/raw/categories.csv', header = true);

CREATE OR REPLACE TABLE bronze_products AS
SELECT * FROM read_csv_auto('data/raw/products.csv', header = true);

CREATE OR REPLACE TABLE bronze_orders AS
SELECT * FROM read_csv_auto('data/raw/orders.csv', header = true);

CREATE OR REPLACE TABLE bronze_order_items AS
SELECT * FROM read_csv_auto('data/raw/order_items.csv', header = true);
