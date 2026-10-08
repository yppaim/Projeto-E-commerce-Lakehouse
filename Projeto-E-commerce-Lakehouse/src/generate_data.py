from pathlib import Path
import random
import pandas as pd

SEED = 42
N_CUSTOMERS = 100
N_ORDERS = 500
START_DATE = pd.Timestamp("2026-01-01")

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw"
RAW_PATH.mkdir(parents=True, exist_ok=True)

first_names = [
    "Ana", "Carlos", "Marina", "João", "Lucas", "Beatriz", "Rafael",
    "Camila", "Felipe", "Juliana", "Gustavo", "Larissa", "Bruno", "Amanda",
    "Diego", "Fernanda", "Thiago", "Gabriela", "Pedro", "Isabela"
]
last_names = [
    "Silva", "Souza", "Costa", "Santos", "Oliveira", "Pereira", "Almeida",
    "Ferreira", "Rodrigues", "Gomes"
]
cities_states = [
    ("São Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Curitiba", "PR"),
    ("Belo Horizonte", "MG"), ("Porto Alegre", "RS"), ("Salvador", "BA"),
    ("Recife", "PE"), ("Fortaleza", "CE"), ("Goiânia", "GO"), ("Brasília", "DF")
]

def build_data():
    rng = random.Random(SEED)

    customers = []
    for customer_id in range(1, N_CUSTOMERS + 1):
        city, state = rng.choice(cities_states)
        customers.append([customer_id, f"{rng.choice(first_names)} {rng.choice(last_names)}", city, state])
    customers = pd.DataFrame(customers, columns=["customer_id", "name", "city", "state"])

    categories = pd.DataFrame([
        [1, "Eletrônicos"], [2, "Livros"], [3, "Casa"], [4, "Escritório"], [5, "Acessórios"]
    ], columns=["category_id", "category_name"])

    product_catalog = [
        ("Notebook", 4500.00, 1), ("Monitor", 1600.00, 1), ("Smartphone", 2800.00, 1),
        ("Fone Bluetooth", 250.00, 1), ("SSD 1TB", 550.00, 1), ("Webcam", 320.00, 1),
        ("SQL para Iniciantes", 80.00, 2), ("Livro Python", 100.00, 2),
        ("Engenharia de Dados", 120.00, 2), ("Data Science na Prática", 110.00, 2),
        ("Clean Code", 150.00, 2), ("Algoritmos", 95.00, 2),
        ("Cadeira Escritório", 900.00, 3), ("Mesa Escritório", 750.00, 3),
        ("Luminária", 140.00, 3), ("Organizador", 65.00, 3),
        ("Garrafa Térmica", 90.00, 3), ("Suporte Monitor", 180.00, 3),
        ("Teclado Mecânico", 350.00, 4), ("Mouse Gamer", 150.00, 4),
        ("Mousepad", 70.00, 4), ("Hub USB", 110.00, 4),
        ("Cabo HDMI", 55.00, 5), ("Adaptador USB-C", 75.00, 5),
        ("Carregador", 130.00, 5), ("Mochila Notebook", 220.00, 5),
        ("Pen Drive 128GB", 85.00, 5), ("Suporte Celular", 60.00, 5),
        ("Cabo USB-C", 45.00, 5), ("Película", 35.00, 5)
    ]
    products = pd.DataFrame(
        [[i, name, price, category] for i, (name, price, category) in enumerate(product_catalog, 1)],
        columns=["product_id", "product_name", "price", "category_id"]
    )

    orders, order_items = [], []
    for order_id in range(1, N_ORDERS + 1):
        customer_id = rng.randint(1, N_CUSTOMERS)
        order_date = START_DATE + pd.Timedelta(days=rng.randint(0, 179))
        orders.append([order_id, customer_id, order_date.strftime("%Y-%m-%d")])
        selected = rng.sample(range(1, len(products) + 1), rng.randint(1, 5))
        for product_id in selected:
            order_items.append([order_id, product_id, rng.randint(1, 4)])

    orders = pd.DataFrame(orders, columns=["order_id", "customer_id", "order_date"])
    order_items = pd.DataFrame(order_items, columns=["order_id", "product_id", "quantity"])
    return customers, categories, products, orders, order_items


def main():
    customers, categories, products, orders, order_items = build_data()
    for name, frame in {
        "customers": customers, "categories": categories, "products": products,
        "orders": orders, "order_items": order_items,
    }.items():
        frame.to_csv(RAW_PATH / f"{name}.csv", index=False)
    print("Dados RAW criados com sucesso.")
    print(f"Clientes: {len(customers):,}")
    print(f"Produtos: {len(products):,}")
    print(f"Pedidos: {len(orders):,}")
    print(f"Itens de pedidos: {len(order_items):,}")


if __name__ == "__main__":
    main()
