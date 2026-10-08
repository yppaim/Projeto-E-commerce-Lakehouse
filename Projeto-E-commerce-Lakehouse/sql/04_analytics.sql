-- Consultas de negócio sobre gold_sales.

-- 1. Faturamento total
SELECT ROUND(SUM(total_amount), 2) AS total_revenue FROM gold_sales;

-- 2. Pedidos e itens
SELECT COUNT(DISTINCT order_id) AS total_orders, COUNT(*) AS total_order_items FROM gold_sales;

-- 3. Ticket médio
SELECT ROUND(SUM(total_amount) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS average_order_value FROM gold_sales;

-- 4. Produtos mais vendidos
SELECT product_name, SUM(quantity) AS units_sold
FROM gold_sales GROUP BY product_name
ORDER BY units_sold DESC, product_name;

-- 5. Produtos com maior faturamento
SELECT product_name, ROUND(SUM(total_amount), 2) AS revenue
FROM gold_sales GROUP BY product_name
ORDER BY revenue DESC, product_name;

-- 6. Faturamento por cidade
SELECT city, ROUND(SUM(total_amount), 2) AS revenue
FROM gold_sales GROUP BY city ORDER BY revenue DESC, city;

-- 7. Faturamento por estado
SELECT state, ROUND(SUM(total_amount), 2) AS revenue
FROM gold_sales GROUP BY state ORDER BY revenue DESC, state;

-- 8. Faturamento por categoria
SELECT category_name, ROUND(SUM(total_amount), 2) AS revenue
FROM gold_sales GROUP BY category_name ORDER BY revenue DESC, category_name;

-- 9. Clientes que mais gastaram
SELECT customer_name, COUNT(DISTINCT order_id) AS orders_count, ROUND(SUM(total_amount), 2) AS total_spent
FROM gold_sales GROUP BY customer_name ORDER BY total_spent DESC, customer_name;

-- 10. Ranking de produtos por faturamento
SELECT product_name, ROUND(SUM(total_amount), 2) AS revenue,
       RANK() OVER (ORDER BY SUM(total_amount) DESC) AS ranking
FROM gold_sales GROUP BY product_name ORDER BY ranking, product_name;

-- 11. Faturamento mensal
SELECT DATE_TRUNC('month', order_date) AS month_start, ROUND(SUM(total_amount), 2) AS revenue
FROM gold_sales GROUP BY month_start ORDER BY month_start;

-- 12. Comparação com o mês anterior
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month_start, ROUND(SUM(total_amount), 2) AS revenue
    FROM gold_sales GROUP BY month_start
), with_previous AS (
    SELECT month_start, revenue, LAG(revenue) OVER (ORDER BY month_start) AS previous_month
    FROM monthly_sales
)
SELECT month_start, revenue, previous_month,
       ROUND(100.0 * (revenue - previous_month) / NULLIF(previous_month, 0), 2) AS month_over_month_pct
FROM with_previous ORDER BY month_start;

-- 13. Participação das categorias
WITH category_revenue AS (
    SELECT category_name, SUM(total_amount) AS revenue
    FROM gold_sales GROUP BY category_name
)
SELECT category_name, ROUND(revenue, 2) AS revenue,
       ROUND(100.0 * revenue / NULLIF(SUM(revenue) OVER (), 0), 2) AS revenue_share_pct
FROM category_revenue ORDER BY revenue DESC;
