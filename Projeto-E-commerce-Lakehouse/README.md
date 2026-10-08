# 🛒 E-commerce Lakehouse

Projeto de portfólio de Engenharia de Dados que simula um pipeline de e-commerce em arquitetura Lakehouse: **Raw → Bronze → Silver → Gold**.

## Objetivos

- gerar dados sintéticos e determinísticos;
- ingerir CSV em DuckDB;
- tratar e tipar dados em Silver;
- criar `gold_sales` em granularidade de item;
- validar qualidade;
- exportar camadas em Parquet;
- executar análises SQL com funções de janela.

## Estrutura

```text
Projeto-E-commerce-Lakehouse/
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── docs/
├── notebooks/
├── sql/
│   ├── 01_bronze.sql
│   ├── 02_silver.sql
│   ├── 03_gold.sql
│   └── 04_analytics.sql
├── src/
│   ├── generate_data.py
│   └── run_pipeline.py
├── tests/
├── requirements.txt
└── README.md
```

## Como executar

### 1. Ambiente

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 2. Dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Gerar dados

```bash
python src/generate_data.py
```

### 4. Executar pipeline

```bash
python src/run_pipeline.py
```

O pipeline cria `ecommerce.duckdb`, executa os checks de qualidade e grava Parquet em `data/bronze`, `data/silver` e `data/gold`.

### 5. Análises

Execute `sql/04_analytics.sql` no DuckDB para consultar os KPIs, rankings, evolução mensal e participação por categoria.

## Correções aplicadas

- Estrutura do repositório normalizada: o conteúdo do projeto agora fica na raiz do ZIP.
- Pipeline independente do diretório atual (`cwd` corrigido).
- Exportação efetiva das camadas para Parquet, alinhada à documentação.
- Validações ampliadas para chaves, relacionamentos, preços, quantidades e existência da Gold.
- Geração de dados encapsulada em função determinística, facilitando testes.
- SQL analítico revisado e organizado.
- Documentação e comandos de execução revisados.

## Tecnologias

Python · Pandas · DuckDB · SQL · Parquet/PyArrow · Git/GitHub

## Autor

Yuri Pereira Paim
