from src.calculate import calculate_order_total

def main():
    orders = [
        {"Product": "Laptop", "Quantity": 2, "Price": 50000},
        {"Product": "Mobile", "Quantity": 0, "Price": 15000},
        {"Product": "Headphones", "Quantity": 3, "Price": "abc"},
        {"Product": "Keyboard", "Quantity": 4, "Price": 2000},
        {"Product": "", "Quantity": 2, "Price": 1000},
    ]

    for idx, order in enumerate(orders, start=1):
        try:
            product, total = calculate_order_total(order, idx)
            print(f"Total for {product} is {total}")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
