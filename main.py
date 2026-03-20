"""TPP Sari-Sari Store (CLI)

This project grows module-by-module (Py4E aligned).
Start point: a simple menu that will expand over time.

Run:
  python main.py
"""


def run_sukli_calculator():
    """Module 01: Sukli Calculator — input item, price, qty, cash; print receipt with change."""
    item = input("Item: ").strip()
    price = float(input("Price: ").strip())
    qty = float(input("Qty: ").strip())
    cash = float(input("Cash: ").strip())

    total = price * qty
    change = cash - total

    print("\n--- Receipt ---")
    print(f"Item: {item}")
    print(f"Price: {price}")
    print(f"Qty: {qty}")
    print(f"Total: {total}")
    print(f"Cash: {cash}")
    print(f"Change: {change}")


def main():
    """Module 01: Sukli Calculator — receipt flow is the main flow."""
    run_sukli_calculator()


if __name__ == "__main__":
    main()
