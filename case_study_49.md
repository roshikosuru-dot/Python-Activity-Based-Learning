# Case Study 49: Tuple-Based Product Catalogue Audit

## 1. Problem Statement
Store product records as immutable tuples containing product ID, product name, unit price, stock quantity, and reorder threshold. Audit the catalogue to detect invalid records, calculate total valid inventory value, and identify products requiring replenishment.

## 2. Objectives
- To store structured product records as tuples inside a list.
- To use tuple unpacking to access fields cleanly during iteration.
- To detect invalid records (negative prices/quantities or duplicate IDs), compute total inventory valuation, and flag low-stock items.

## 3. Assumptions
- Each product tuple has the format: (product_id, name, unit_price, stock_qty, reorder_level).
- A record is invalid if product_id is duplicated, unit_price <= 0, stock_qty < 0, or reorder_level < 0.
- Valid products with stock_qty <= reorder_level require immediate replenishment.

## 4. Algorithm
1. Start the program.
2. Input number of product records n and read each record into a tuple appended to catalogue.
3. Initialize empty lists seen_ids, invalid_records, reorder_list, and total_inventory_value = 0.0.
4. Loop through catalogue using tuple unpacking (pid, name, price, qty, reorder):
5.   If pid in seen_ids or price <= 0 or qty < 0 or reorder < 0: record in invalid_records.
6.   Else: add pid to seen_ids, add (price * qty) to total_inventory_value, and if qty <= reorder, append to reorder_list.
7. Print audit report showing invalid records, total inventory value, and replenishment alerts.
8. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
[ Read n Product Tuples into catalogue ]
           |
           v
 < Unpack (pid, name, price, qty, reorder) > -- Done --> [ Print Audit Report ]
           |                                                      |
          Next                                                    v
           |                                                   [ End ]
           v
< Duplicate ID or price<=0 or qty<0 ? > -- Yes --> [ Log Invalid Record ]
           |
          No
           |
           v
[ total_value += price * qty ]
           |
           v
  < qty <= reorder ? > -- Yes --> [ Add to Replenishment List ]
```

## 6. Pseudocode
```text
BEGIN
    READ n
    SET catalogue = []
    FOR i FROM 1 TO n DO
        READ pid, name, price, qty, reorder
        APPEND (pid, name, price, qty, reorder) TO catalogue
    ENDFOR

    SET seen_ids = []
    SET total_value = 0.0
    SET invalid_list = []
    SET reorder_list = []

    FOR EACH (pid, name, price, qty, reorder) IN catalogue DO
        IF pid IN seen_ids OR price <= 0 OR qty < 0 OR reorder < 0 THEN
            APPEND (pid, name) TO invalid_list
        ELSE
            APPEND pid TO seen_ids
            SET total_value = total_value + (price * qty)
            IF qty <= reorder THEN
                APPEND (pid, name, qty, reorder) TO reorder_list
            ENDIF
        ENDIF
    ENDFOR

    PRINT invalid_list, total_value, reorder_list
END
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
- **Record 1:** `("P101", "Wireless Mouse", 650.0, 8, 10)` -> Valid, value = Rs. 5,200, flagged for replenishment (`8 <= 10`).
- **Record 2:** `("P102", "Mechanical Keyboard", 2400.0, 15, 5)` -> Valid, value = Rs. 36,000, sufficient stock.
- **Record 3:** `("P101", "USB Hub", 500.0, 20, 5)` -> Invalid (Duplicate Product ID `P101`).
- **Record 4:** `("P103", "Webcam", -1200.0, 4, 5)` -> Invalid (Negative unit price).

## 9. Sample Output
```text
Enter number of product records to audit: 4

Product 1:
  Product ID: P101
  Product Name: Wireless Mouse
  Unit Price (Rs.): 650
  Stock Quantity: 8
  Reorder Threshold: 10

Product 2:
  Product ID: P102
  Product Name: Mechanical Keyboard
  Unit Price (Rs.): 2400
  Stock Quantity: 15
  Reorder Threshold: 5

Product 3:
  Product ID: P101
  Product Name: USB Hub
  Unit Price (Rs.): 500
  Stock Quantity: 20
  Reorder Threshold: 5

Product 4:
  Product ID: P103
  Product Name: Webcam
  Unit Price (Rs.): -1200
  Stock Quantity: 4
  Reorder Threshold: 5

================ PRODUCT CATALOGUE AUDIT REPORT ================
Total Valid Inventory Value: Rs. 41,200.00

1. Invalid Records Detected:
   - [P101] USB Hub: Duplicate Product ID
   - [P103] Webcam: Invalid price (Rs. -1200.0)

2. Items Requiring Replenishment:
   - [P101] Wireless Mouse: Stock = 8 (Threshold = 10)
================================================================
```

## 10. Conclusion
Using tuples to represent immutable product records and tuple unpacking for validation ensures clean, readable auditing of inventory data.
