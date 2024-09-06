def process_orders(order_list):
    for order in order_list:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),

]

process_orders(orders)

