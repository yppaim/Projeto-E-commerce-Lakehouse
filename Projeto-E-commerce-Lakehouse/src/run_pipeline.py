from pathlib import Path
import os
import duckdb

ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "ecommerce.duckdb"
SCRIPTS = [ROOT / "sql" / name for name in ("01_bronze.sql", "02_silver.sql", "03_gold.sql")]
PARQUET_TARGETS = {
    "bronze": ["customers", "categories", "products", "orders", "order_items"],
    "silver": ["customers", "categories", "products", "orders", "order_items"],
    "gold": ["sales"],
}

def run_sql_script(con, script_path):
    print(f"[INFO] Executando {script_path.relative_to(ROOT)}")
    con.execute(script_path.read_text(encoding="utf-8"))

def export_parquet(con):
    for layer, tables in PARQUET_TARGETS.items():
        target_dir = ROOT / "data" / layer
        target_dir.mkdir(parents=True, exist_ok=True)
        for table in tables:
            table_name = f"{layer}_{table}"
            if layer == "gold":
                table_name = "gold_sales"
            output = target_dir / f"{table}.parquet"
            con.execute(f"COPY {table_name} TO '{output.as_posix()}' (FORMAT PARQUET)")

def run_quality_checks(con):
    checks = {
        "Gold possui registros": "SELECT COUNT(*) > 0 FROM gold_sales",
        "customer_id sem nulos": "SELECT COUNT(*) = 0 FROM silver_customers WHERE customer_id IS NULL",
        "customer_id único": "SELECT COUNT(*) = COUNT(DISTINCT customer_id) FROM silver_customers",
        "product_id sem nulos": "SELECT COUNT(*) = 0 FROM silver_products WHERE product_id IS NULL",
        "category_id sem nulos": "SELECT COUNT(*) = 0 FROM silver_categories WHERE category_id IS NULL",
        "preços não negativos": "SELECT COUNT(*) = 0 FROM silver_products WHERE price < 0",
        "quantidades maiores que zero": "SELECT COUNT(*) = 0 FROM silver_order_items WHERE quantity <= 0",
        "pedidos com cliente válido": """SELECT COUNT(*) = 0 FROM silver_orders o
            LEFT JOIN silver_customers c ON o.customer_id = c.customer_id
            WHERE c.customer_id IS NULL""",
        "itens com pedido válido": """SELECT COUNT(*) = 0 FROM silver_order_items i
            LEFT JOIN silver_orders o ON i.order_id = o.order_id
            WHERE o.order_id IS NULL""",
        "itens com produto válido": """SELECT COUNT(*) = 0 FROM silver_order_items i
            LEFT JOIN silver_products p ON i.product_id = p.product_id
            WHERE p.product_id IS NULL""",
        "produtos com categoria válida": """SELECT COUNT(*) = 0 FROM silver_products p
            LEFT JOIN silver_categories c ON p.category_id = c.category_id
            WHERE c.category_id IS NULL""",
    }
    failures = []
    for name, query in checks.items():
        passed = bool(con.execute(query).fetchone()[0])
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        if not passed:
            failures.append(name)
    if failures:
        raise RuntimeError("Validações de qualidade falharam: " + ", ".join(failures))

def main():
    raw_path = ROOT / "data" / "raw"
    if not raw_path.exists() or len(list(raw_path.glob("*.csv"))) < 5:
        raise FileNotFoundError("Execute primeiro: python src/generate_data.py")

    # Os scripts SQL usam caminhos relativos; fixamos o cwd para tornar
    # a execução independente do diretório a partir do qual o comando foi chamado.
    os.chdir(ROOT)
    con = duckdb.connect(str(DATABASE))
    try:
        for script in SCRIPTS:
            run_sql_script(con, script)
        run_quality_checks(con)
        export_parquet(con)
        rows, revenue = con.execute(
            "SELECT COUNT(*), ROUND(SUM(total_amount), 2) FROM gold_sales"
        ).fetchone()
        print(f"[INFO] Linhas na Gold: {rows:,}")
        print(f"[INFO] Receita total: R$ {revenue:,.2f}")
        print("[INFO] Pipeline concluído com sucesso!")
    finally:
        con.close()

if __name__ == "__main__":
    main()
