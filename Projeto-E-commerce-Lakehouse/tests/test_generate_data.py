from src.generate_data import build_data

def test_deterministic_shape_and_keys():
    customers, categories, products, orders, items = build_data()
    assert len(customers) == 100
    assert len(categories) == 5
    assert len(products) == 30
    assert len(orders) == 500
    assert len(items) == 1454
    assert customers.customer_id.is_unique
    assert products.product_id.is_unique
    assert orders.order_id.is_unique
