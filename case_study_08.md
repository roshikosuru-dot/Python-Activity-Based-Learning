# CASE STUDY 49: TUPLE-BASED PRODUCT CATALOGUE AUDIT

---

## 1. PROBLEM STATEMENT

Store product records as immutable tuples containing product ID, product name, unit price, stock quantity, and reorder threshold. Audit the catalogue to detect invalid records, calculate the total valid inventory value, and identify products requiring replenishment.

---

## 2. OBJECTIVES

- To store structured product records as tuples inside a list.
- To use tuple unpacking to access fields during iteration.
- To detect invalid records such as duplicate IDs, non-positive prices, and negative quantities or reorder thresholds.
- To calculate the total inventory value of valid products.
- To identify products requiring replenishment.

---

## 3. ASSUMPTIONS

| S.No. | Assumption | Description |
|---|---|---|
| 1 | Data Structure | Product records are stored as tuples inside a list. |
| 2 | Tuple Format | `(product_id, name, unit_price, stock_qty, reorder_level)` |
| 3 | Duplicate ID | A product ID must be unique. |
| 4 | Price Validation | Unit price must be greater than zero. |
| 5 | Stock Validation | Stock quantity must not be negative. |
| 6 | Reorder Validation | Reorder threshold must not be negative. |
| 7 | Inventory Value | Only valid records are included in the total valuation. |
| 8 | Replenishment | Valid products with `stock_qty <= reorder_level` require replenishment. |

---

## 4. ALGORITHM

1. START the program.
2. INPUT the number of product records `n`.
3. CREATE an empty list named `catalogue`.
4. READ product ID, product name, unit price, stock quantity, and reorder threshold for each product.
5. STORE each product as a tuple inside the catalogue list.
6. INITIALIZE:
   - `seen_ids = []`
   - `invalid_records = []`
   - `reorder_items = []`
   - `total_inventory_value = 0.0`
7. ITERATE through the catalogue using tuple unpacking.
8. CHECK whether the product ID is duplicated.
9. CHECK whether the unit price is less than or equal to zero.
10. CHECK whether the stock quantity or reorder threshold is negative.
11. IF any validation condition is true:
    - ADD the record and its reason to `invalid_records`.
12. ELSE:
    - ADD the product ID to `seen_ids`.
    - CALCULATE `price * qty`.
    - UPDATE the total inventory value.
    - IF `qty <= reorder`, ADD the product to `reorder_items`.
13. DISPLAY invalid records, total inventory value, and replenishment alerts.
14. STOP the program.

---

## 5. FLOWCHART

```text
                 +-------------+
                 |    START    |
                 +-------------+
                        |
                        v
          +---------------------------+
          | Input Number of Products |
          +---------------------------+
                        |
                        v
          +---------------------------+
          | Read Product Records      |
          | Store Records as Tuples   |
          +---------------------------+
                        |
                        v
          +---------------------------+
          | Initialize Audit Lists    |
          | and Total Inventory Value |
          +---------------------------+
                        |
                        v
               +----------------+
               | More Records?  |
               +----------------+
                  /          \
                Yes           No
                 |             |
                 v             v
       +----------------+  +--------------------+
       | Unpack Product |  | Display Audit      |
       | Tuple          |  | Report             |
       +----------------+  +--------------------+
                 |                  |
                 v                  v
       +--------------------+  +-------------+
       | Validate Product   |  |     END     |
       | Record             |  +-------------+
       +--------------------+
                 |
                 v
       +-------------------------+
       | Duplicate ID or Invalid |
       | Price / Quantity / Level?|
       +-------------------------+
             /             \
           Yes              No
            |                |
            v                v
   +----------------+  +-------------------+
   | Log Invalid    |  | Add ID to         |
   | Record         |  | Seen IDs          |
   +----------------+  +-------------------+
            |                |
            |                v
            |       +-------------------+
            |       | Calculate Price   |
            |       | x Quantity        |
            |       +-------------------+
            |                |
            |                v
            |       +-------------------+
            |       | Update Total      |
            |       | Inventory Value   |
            |       +-------------------+
            |                |
            |                v
            |       +-------------------+
            |       | Stock <= Reorder  |
            |       | Level?            |
            |       +-------------------+
            |          /          \
            |        Yes           No
            |         |             |
            |         v             |
            |  +----------------+   |
            |  | Add to Reorder |   |
            |  | List           |   |
            |  +----------------+   |
            |         |             |
            +---------+-------------+
                      |
                      v
              +----------------+
              | Next Record    |
              +----------------+
                      |
                      +----> Repeat
```

---

## 6. PSEUDOCODE

```text
BEGIN

    READ n
    SET catalogue = []

    FOR i FROM 1 TO n DO
        READ pid, name, price, qty, reorder
        APPEND (pid, name, price, qty, reorder)
        TO catalogue
    ENDFOR

    SET seen_ids = []
    SET total_value = 0.0
    SET invalid_list = []
    SET reorder_list = []

    FOR EACH (pid, name, price, qty, reorder)
    IN catalogue DO

        IF pid IN seen_ids THEN
            APPEND (pid, name, "Duplicate Product ID")
            TO invalid_list

        ELSE IF price <= 0 THEN
            APPEND (pid, name, "Invalid Price")
            TO invalid_list

        ELSE IF qty < 0 OR reorder < 0 THEN
            APPEND (pid, name, "Negative Stock or Reorder Level")
            TO invalid_list

        ELSE
            APPEND pid TO seen_ids

            SET total_value = total_value + (price * qty)

            IF qty <= reorder THEN
                APPEND (pid, name, qty, reorder)
                TO reorder_list
            ENDIF

        ENDIF

    ENDFOR

    PRINT invalid_list
    PRINT total_value
    PRINT reorder_list

END
```

---

## 7. PYTHON SOURCE CODE

```python
# Case Study 49: Tuple-Based Product Catalogue Audit

n = int(input("Enter number of product records to audit: "))
catalogue = []

# Read product records and store them as tuples
for i in range(1, n + 1):
    print(f"\nProduct {i}:")

    pid = input("  Product ID: ").strip().upper()
    name = input("  Product Name: ").strip()
    price = float(input("  Unit Price (Rs.): "))
    qty = int(input("  Stock Quantity: "))
    reorder = int(input("  Reorder Threshold: "))

    record = (pid, name, price, qty, reorder)
    catalogue.append(record)

# Initialize audit variables
seen_ids = []
invalid_records = []
reorder_items = []
total_inventory_value = 0.0

# Audit catalogue using tuple unpacking
for pid, name, price, qty, reorder in catalogue:

    if pid in seen_ids:
        invalid_records.append(
            (pid, name, "Duplicate Product ID")
        )

    elif price <= 0:
        invalid_records.append(
            (pid, name, f"Invalid price (Rs. {price})")
        )

    elif qty < 0 or reorder < 0:
        invalid_records.append(
            (pid, name, "Negative stock or reorder level")
        )

    else:
        seen_ids.append(pid)

        total_inventory_value += price * qty

        if qty <= reorder:
            reorder_items.append(
                (pid, name, qty, reorder)
            )

# Display audit report
print("\n================ PRODUCT CATALOGUE AUDIT REPORT ================")

print(
    f"Total Valid Inventory Value: "
    f"Rs. {total_inventory_value:,.2f}"
)

print("\n1. Invalid Records Detected:")

if len(invalid_records) == 0:
    print("   None")
else:
    for pid, name, reason in invalid_records:
        print(f"   - [{pid}] {name}: {reason}")

print("\n2. Items Requiring Replenishment:")

if len(reorder_items) == 0:
    print("   All valid items have sufficient stock.")
else:
    for pid, name, qty, reorder in reorder_items:
        print(
            f"   - [{pid}] {name}: Stock = {qty} "
            f"(Threshold = {reorder})"
        )

print("================================================================")
```

---

## 8. TEST CASES

### Test Case 1: Product Catalogue Records

| Record | Product ID | Product Name | Price (Rs.) | Quantity | Reorder Level | Result |
|---|---|---|---:|---:|---:|---|
| 1 | P101 | Wireless Mouse | 650 | 8 | 10 | Valid |
| 2 | P102 | Mechanical Keyboard | 2400 | 15 | 5 | Valid |
| 3 | P101 | USB Hub | 500 | 20 | 5 | Invalid: Duplicate ID |
| 4 | P103 | Webcam | -1200 | 4 | 5 | Invalid: Invalid Price |

### Test Case 2: Inventory Value Calculation

```text
Wireless Mouse
= 650 x 8
= Rs. 5,200

Mechanical Keyboard
= 2400 x 15
= Rs. 36,000

Total Inventory Value
= 5,200 + 36,000
= Rs. 41,200
```

### Test Case 3: Replenishment Check

| Product | Stock Quantity | Reorder Level | Status |
|---|---:|---:|---|
| Wireless Mouse | 8 | 10 | Replenishment Required |
| Mechanical Keyboard | 15 | 5 | Sufficient Stock |

### Expected Results

| S.No. | Expected Result | Actual Result |
|---|---|---|
| 1 | P101 Wireless Mouse is valid | Valid |
| 2 | P102 Mechanical Keyboard is valid | Valid |
| 3 | Duplicate P101 is rejected | Invalid |
| 4 | Negative price is rejected | Invalid |
| 5 | Total inventory value is Rs. 41,200 | Rs. 41,200 |
| 6 | Wireless Mouse is flagged for replenishment | Flagged |

---

## 9. SAMPLE OUTPUT

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

---

## 10. CONCLUSION

The Tuple-Based Product Catalogue Audit demonstrates how Python tuples can store structured and immutable product records. Tuple unpacking makes record processing simple and readable, while validation helps identify duplicate product IDs and invalid numerical values.

The program calculates the total value of valid inventory and identifies products that require replenishment. This approach provides a clear and organized method for basic inventory auditing using Python lists, tuples, loops, and conditional statements.

---

**END OF CASE STUDY 49**
