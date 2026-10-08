# Arquitetura do E-commerce Lakehouse

```text
Dados simulados (Python)
        │
        ▼
      RAW (CSV)
        │
        ▼
   BRONZE (DuckDB + Parquet)
        │
   limpeza + tipagem
        ▼
   SILVER (DuckDB + Parquet)
        │
      integração
        ▼
   GOLD / gold_sales (DuckDB + Parquet)
        │
        ├── SQL Analytics
        └── BI / Dashboard
```

## Responsabilidades

- **Raw:** dados de origem gerados de forma determinística.
- **Bronze:** ingestão preservando a estrutura de origem.
- **Silver:** limpeza, padronização e conversão de tipos.
- **Gold:** integração em granularidade de item de pedido.

## Execução

1. `python src/generate_data.py` cria os cinco CSVs em `data/raw/`.
2. `python src/run_pipeline.py` executa Bronze → Silver → Gold.
3. O pipeline executa validações de qualidade e exporta as camadas para Parquet.
4. `sql/04_analytics.sql` contém as consultas de negócio.

O pipeline foi ajustado para funcionar mesmo quando iniciado fora do diretório raiz do projeto.
