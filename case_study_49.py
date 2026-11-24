# Case Study 49: Tuple-Based Product Catalogue Audit

n = int(input("Enter number of product records to audit: "))
catalogue = []

for i in range(1, n + 1):
    print(f"\nProduct {i}:")
    pid = input("  Product ID: ").strip().upper()
    name = input("  Product Name: ").strip()
    price = float(input("  Unit Price (Rs.): "))
    qty = int(input("  Stock Quantity: "))
    reorder = int(input("  Reorder Threshold: "))
    record = (pid, name, price, qty, reorder)
    catalogue.append(record)

seen_ids = []
invalid_records = []
reorder_items = []
total_inventory_value = 0.0

for pid, name, price, qty, reorder in catalogue:
    if pid in seen_ids:
        invalid_records.append((pid, name, "Duplicate Product ID"))
    elif price <= 0:
        invalid_records.append((pid, name, f"Invalid price (Rs. {price})"))
    elif qty < 0 or reorder < 0:
        invalid_records.append((pid, name, "Negative stock or reorder level"))
    else:
        seen_ids.append(pid)
        total_inventory_value += price * qty
        if qty <= reorder:
            reorder_items.append((pid, name, qty, reorder))

print("
================ PRODUCT CATALOGUE AUDIT REPORT ================")
print(f"Total Valid Inventory Value: Rs. {total_inventory_value:,.2f}")

print("
1. Invalid Records Detected:")
if len(invalid_records) == 0:
    print("   None")
else:
    for pid, name, reason in invalid_records:
        print(f"   - [{pid}] {name}: {reason}")

print("
2. Items Requiring Replenishment:")
if len(reorder_items) == 0:
    print("   All valid items have sufficient stock.")
else:
    for pid, name, qty, reorder in reorder_items:
        print(f"   - [{pid}] {name}: Stock = {qty} (Threshold = {reorder})")
print("================================================================")
