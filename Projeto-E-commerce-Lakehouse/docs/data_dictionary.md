# Dicionário de dados

| Entidade | Campo | Tipo | Descrição |
|---|---|---|---|
| customers | customer_id | INTEGER | Identificador do cliente |
| customers | name | VARCHAR | Nome |
| customers | city | VARCHAR | Cidade |
| customers | state | VARCHAR | UF |
| categories | category_id | INTEGER | Identificador da categoria |
| categories | category_name | VARCHAR | Nome da categoria |
| products | product_id | INTEGER | Identificador do produto |
| products | product_name | VARCHAR | Nome do produto |
| products | price | DECIMAL | Preço unitário |
| products | category_id | INTEGER | Categoria do produto |
| orders | order_id | INTEGER | Identificador do pedido |
| orders | customer_id | INTEGER | Cliente do pedido |
| orders | order_date | DATE | Data do pedido |
| order_items | order_id | INTEGER | Pedido relacionado |
| order_items | product_id | INTEGER | Produto relacionado |
| order_items | quantity | INTEGER | Quantidade comprada |
| gold_sales | total_amount | DECIMAL | quantity × price |
