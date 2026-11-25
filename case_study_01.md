Here is **Case Study 2: Progressive Electricity Billing** in a clean box-style format for your `README.md`, suitable for GitHub.

# CASE STUDY 2: PROGRESSIVE ELECTRICITY BILLING

---

## 1. PROBLEM STATEMENT

Design and implement a Python program to calculate household electricity bills across multiple months using progressive consumption slabs, fixed charges, surcharges, and rebates. The system also compares monthly bills to detect unusual increases in electricity consumption.

---

## 2. OBJECTIVES

- Calculate monthly electricity bills using progressive slab rates.
- Apply fixed meter charges, rebates, and surcharges.
- Store monthly electricity consumption and bills in lists.
- Compare consecutive monthly bills.
- Detect and flag unusual increases greater than 30%.

---

## 3. ASSUMPTIONS

| Description      | Value                           |
| ---------------- | ------------------------------- |
| 0–100 units      | Rs. 3.00/unit                   |
| 101–200 units    | Rs. 5.00/unit                   |
| Above 200 units  | Rs. 8.00/unit                   |
| Fixed Charge     | Rs. 50.00                       |
| Rebate           | 5% for consumption ≤ 100 units  |
| Surcharge        | 10% for consumption > 300 units |
| Unusual Increase | More than 30%                   |
| Input Validation | Units must be non-negative      |

---

## 4. ALGORITHM

1. Start the program.
2. Input the number of months.
3. Initialize empty lists `units_list` and `bills`.
4. Read monthly electricity consumption.
5. Validate that units are non-negative.
6. Calculate energy charges using progressive slabs.
7. Apply rebate or surcharge where applicable.
8. Add the fixed charge of Rs. 50.
9. Store monthly units and bills in lists.
10. Display the monthly billing summary.
11. Compare consecutive monthly bills.
12. Display alerts for increases greater than 30%.
13. Stop the program.

---

## 5. FLOWCHART

```
          +----------------+
          |     START      |
          +----------------+
                  |
                  v
       +----------------------+
       | Input Number of      |
       | Months (n)           |
       +----------------------+
                  |
                  v
       +----------------------+
       | Initialize Lists     |
       | units_list, bills    |
       +----------------------+
                  |
                  v
       +----------------------+
       | Input Monthly Units  |
       +----------------------+
                  |
                  v
          +---------------+
          | Units >= 0 ?  |
          +---------------+
             |       |
            No      Yes
             |       |
             v       v
       +----------+  +--------------------+
       | Re-enter |  | Calculate Energy   |
       | Units    |  | Charge             |
       +----------+  +--------------------+
             |                 |
             +-----------------+
                               |
                               v
                    +--------------------+
                    | Apply Rebate /     |
                    | Surcharge           |
                    +--------------------+
                               |
                               v
                    +--------------------+
                    | Add Fixed Charge   |
                    | Rs. 50             |
                    +--------------------+
                               |
                               v
                    +--------------------+
                    | Store Units & Bill |
                    +--------------------+
                               |
                               v
                    +--------------------+
                    | More Months?       |
                    +--------------------+
                         |         |
                        Yes        No
                         |         |
                         +---------+
                           Repeat
                                   |
                                   v
                    +--------------------+
                    | Display Bill       |
                    | Summary            |
                    +--------------------+
                                   |
                                   v
                    +--------------------+
                    | Compare Monthly    |
                    | Bills              |
                    +--------------------+
                                   |
                                   v
                    +--------------------+
                    | Display Spike      |
                    | Alerts             |
                    +--------------------+
                                   |
                                   v
                          +-------------+
                          |     END     |
                          +-------------+
```

---

## 6. PSEUDOCODE

```
BEGIN
    READ n
    SET units_list = []
    SET bills = []

    FOR i FROM 0 TO n-1 DO
        READ units

        WHILE units < 0 DO
            DISPLAY "Invalid units"
            READ units
        ENDWHILE

        IF units <= 100 THEN
            energy = units * 3
        ELSE IF units <= 200 THEN
            energy = 100 * 3 + (units - 100) * 5
        ELSE
            energy = 100 * 3 + 100 * 5
                     + (units - 200) * 8
        ENDIF

        IF units <= 100 THEN
            adjustment = -0.05 * energy
        ELSE IF units > 300 THEN
            adjustment = 0.10 * energy
        ELSE
            adjustment = 0
        ENDIF

        total = energy + adjustment + 50

        APPEND units TO units_list
        APPEND total TO bills
    ENDFOR

    DISPLAY monthly billing summary

    FOR i FROM 1 TO n-1 DO
        IF bills[i-1] > 0 THEN
            increase = ((bills[i] - bills[i-1])
                        / bills[i-1]) * 100

            IF increase > 30 THEN
                DISPLAY "Unusual Increase Alert"
            ENDIF
        ENDIF
    ENDFOR
END
```

---

## 7. PYTHON SOURCE CODE

```
# Case Study 2: Progressive Electricity Billing

n = int(input("Enter number of months to analyze: "))

units_list = []
bills = []

for i in range(n):
    units = int(input(f"Enter units consumed in Month {i + 1}: "))

    while units < 0:
        print("Invalid input. Units cannot be negative.")
        units = int(input("Re-enter units: "))

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + ((units - 100) * 5.0)
    else:
        energy_charge = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 8.0)

    # Rebate and surcharge
    if units <= 100:
        adjustment = -0.05 * energy_charge
    elif units > 300:
        adjustment = 0.10 * energy_charge
    else:
        adjustment = 0.0

    fixed_charge = 50.0
    total_bill = energy_charge + adjustment + fixed_charge

    units_list.append(units)
    bills.append(total_bill)

# Display monthly bills
print("\\n--- Monthly Electricity Bill Summary ---")

for i in range(n):
    print(
        f"Month {i + 1}: Units = {units_list[i]} | "
        f"Total Bill = Rs. {bills[i]:.2f}"
    )

# Detect unusual increases
print("\\n--- Month-over-Month Spike Analysis ---")

spike_found = False

for i in range(1, n):
    if bills[i - 1] > 0:
        pct_change = (
            (bills[i] - bills[i - 1]) / bills[i - 1]
        ) * 100

        if pct_change > 30:
            print(
                f"ALERT: Month {i + 1} bill increased by "
                f"{pct_change:.1f}% compared to Month {i}."
            )
            spike_found = True

if not spike_found:
    print("No unusual bill increases detected.")
```

---

## 8. TEST CASES

| Test Case      | Units | Expected Bill |
| -------------- | ----- | ------------- |
| Rebate Slab    | 80    | Rs. 278.00    |
| Middle Slab    | 180   | Rs. 750.00    |
| Surcharge Slab | 350   | Rs. 2250.00   |

### Calculation

**Test Case 1: 80 Units**

- Energy Charge = 80 × 3 = Rs. 240
- Rebate = 5% of 240 = Rs. 12
- Fixed Charge = Rs. 50
- Total = **Rs. 278.00**

**Test Case 2: 180 Units**

- First 100 units = Rs. 300
- Next 80 units = Rs. 400
- Energy Charge = Rs. 700
- Fixed Charge = Rs. 50
- Total = **Rs. 750.00**

**Test Case 3: 350 Units**

- First 100 units = Rs. 300
- Next 100 units = Rs. 500
- Remaining 150 units = Rs. 1200
- Energy Charge = Rs. 2000
- Surcharge = Rs. 200
- Fixed Charge = Rs. 50
- Total = **Rs. 2250.00**

---

## 9. SAMPLE OUTPUT

```
Enter number of months to analyze: 3
Enter units consumed in Month 1: 80
Enter units consumed in Month 2: 180
Enter units consumed in Month 3: 350

--- Monthly Electricity Bill Summary ---
Month 1: Units = 80 | Total Bill = Rs. 278.00
Month 2: Units = 180 | Total Bill = Rs. 750.00
Month 3: Units = 350 | Total Bill = Rs. 2250.00

--- Month-over-Month Spike Analysis ---
ALERT: Month 2 bill increased by 169.8% compared to Month 1.
ALERT: Month 3 bill increased by 200.0% compared to Month 2.
```

---

## 10. CONCLUSION

The Progressive Electricity Billing System successfully calculates monthly electricity bills using progressive tariff slabs. It applies fixed charges, rebates, and surcharges while storing monthly data in lists. The program also compares consecutive bills and identifies unusual increases greater than 30%, making electricity billing and monitoring more efficient.

---

**END OF CASE STUDY 2**

Put the entire case study in boxesUse separate boxes for each section
