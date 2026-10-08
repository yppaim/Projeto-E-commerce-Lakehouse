# Resultados reproduzíveis

Com `SEED = 42`, o dataset esperado possui:

| Indicador | Resultado |
|---|---:|
| Clientes | 100 |
| Produtos | 30 |
| Pedidos | 500 |
| Itens de pedido | 1.454 |
| Faturamento total | R$ 1.802.480,00 |
| Ticket médio | R$ 3.604,96 |

Os resultados são dados sintéticos e podem ser reproduzidos com `python src/generate_data.py` seguido de `python src/run_pipeline.py`.
