# Case Study 2: Progressive Electricity Billing

## 1. Problem Statement
Design and implement a Python program to calculate household electricity bills across multiple months using progressive consumption slabs, fixed charges, surcharges, and rebates. The system must also compare monthly bills to detect and flag unusual spikes in electricity consumption.

## 2. Objectives
- To compute accurate monthly electricity bills using progressive slab rates.
- To apply fixed meter charges, low-consumption rebates, and high-consumption surcharges.
- To store monthly bills in a list and analyze month-over-month variations to detect unusual increases.

## 3. Assumptions
- Units consumed in any month are non-negative integers.
- Progressive Tariff Slabs: 0-100 units @ Rs. 3.00/unit, 101-200 units @ Rs. 5.00/unit, >200 units @ Rs. 8.00/unit.
- Fixed Charge: Rs. 50.00 per month added to every bill.
- Rebate: 5% discount on energy charges if monthly consumption is 100 units or less.
- Surcharge: 10% surcharge on energy charges if monthly consumption exceeds 300 units.
- Unusual Increase: An increase of more than 30% compared to the immediately preceding month is flagged.

## 4. Algorithm
1. Start the program.
2. Input the number of months n to be analyzed.
3. Initialize empty lists units_list and bills.
4. For each month i from 0 to n - 1: input units and validate units >= 0.
5. Compute energy_charge using progressive slabs (0-100, 101-200, >200).
6. Apply 5% rebate if units <= 100, or 10% surcharge if units > 300.
7. Add fixed charge of Rs. 50.00 to compute total_bill and append to bills.
8. Display the monthly billing summary.
9. Compare consecutive bills (i from 1 to n - 1) and flag any month with >30% increase.
10. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
  / Input n (months) /
           |
           v
[ Initialize bills = [] ]
           |
           v
  < i < n ? > ---- No ----> [ Loop i = 1 to n-1: Compare bills[i] & bills[i-1] ]
       |                                              |
      Yes                                             v
       |                                     / Display Spike Alerts /
       v                                              |
/ Input units for Month i+1 /                         v
       |                                           [ End ]
       v
[ Calculate Slab Energy Charge ]
       |
       v
[ Apply Rebate (<=100) / Surcharge (>300) + Rs. 50 Fixed ]
       |
       v
[ Append total_bill to bills, i = i + 1 ]
       |
       +---------> (Loop back to < i < n ? >)
```

## 6. Pseudocode
```text
BEGIN
    READ n
    SET bills = []
    SET units_list = []

    FOR i FROM 0 TO n - 1 DO
        READ units
        IF units <= 100 THEN
            SET energy = units * 3.0
        ELSE IF units <= 200 THEN
            SET energy = (100 * 3.0) + ((units - 100) * 5.0)
        ELSE
            SET energy = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 8.0)
        ENDIF

        IF units <= 100 THEN
            SET adj = -0.05 * energy
        ELSE IF units > 300 THEN
            SET adj = 0.10 * energy
        ELSE
            SET adj = 0.0
        ENDIF

        SET total = energy + adj + 50.0
        APPEND units TO units_list
        APPEND total TO bills
    ENDFOR

    FOR i FROM 0 TO n - 1 DO
        PRINT "Month", i + 1, units_list[i], bills[i]
    ENDFOR

    FOR i FROM 1 TO n - 1 DO
        SET increase = ((bills[i] - bills[i - 1]) / bills[i - 1]) * 100
        IF increase > 30.0 THEN
            PRINT "Alert: Unusual increase in Month", i + 1
        ENDIF
    ENDFOR
END
```

## 7. Python Source Code
```python
# Case Study 2: Progressive Electricity Billing

n = int(input("Enter number of months to analyze: "))
units_list = []
bills = []

for i in range(n):
    units = int(input(f"Enter units consumed in Month {i + 1}: "))
    while units < 0:
        print("Invalid input. Units cannot be negative.")
        units = int(input(f"Re-enter units consumed in Month {i + 1}: "))

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + ((units - 100) * 5.0)
    else:
        energy_charge = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 8.0)

    # Rebate and surcharge calculation
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

print("\n--- Monthly Electricity Bill Summary ---")
for i in range(n):
    print(f"Month {i + 1}: Units = {units_list[i]} | Total Bill = Rs. {bills[i]:.2f}")

print("\n--- Month-over-Month Spike Analysis ---")
spike_found = False
for i in range(1, n):
    if bills[i - 1] > 0:
        pct_change = ((bills[i] - bills[i - 1]) / bills[i - 1]) * 100
        if pct_change > 30.0:
            print(
                f"ALERT: Month {i + 1} bill (Rs. {bills[i]:.2f}) increased by "
                f"{pct_change:.1f}% compared to Month {i} (Rs. {bills[i - 1]:.2f})."
            )
            spike_found = True

if not spike_found:
    print("No unusual bill increases (>30%) detected.")
```

## 8. Test Cases
- **Test Case 1 (Rebate Slab):** 80 units -> Energy: Rs. 240.00, Rebate (5%): -Rs. 12.00, Fixed: Rs. 50.00 -> **Rs. 278.00**.
- **Test Case 2 (Mid Slab):** 180 units -> Energy: Rs. 300.00 + Rs. 400.00 = Rs. 700.00, Fixed: Rs. 50.00 -> **Rs. 750.00**.
- **Test Case 3 (Surcharge & Spike):** 350 units -> Energy: Rs. 2000.00, Surcharge (10%): +Rs. 200.00, Fixed: Rs. 50.00 -> **Rs. 2250.00** (Triggers spike alert).

## 9. Sample Output
```text
Enter number of months to analyze: 3
Enter units consumed in Month 1: 80
Enter units consumed in Month 2: 180
Enter units consumed in Month 3: 350

--- Monthly Electricity Bill Summary ---
Month 1: Units = 80 | Total Bill = Rs. 278.00
Month 2: Units = 180 | Total Bill = Rs. 750.00
Month 3: Units = 350 | Total Bill = Rs. 2250.00

--- Month-over-Month Spike Analysis ---
ALERT: Month 2 bill (Rs. 750.00) increased by 169.8% compared to Month 1 (Rs. 278.00).
ALERT: Month 3 bill (Rs. 2250.00) increased by 200.0% compared to Month 2 (Rs. 750.00).
```

## 10. Conclusion
The progressive electricity billing system successfully calculates tiered tariffs, applies conditional rebates and surcharges, and uses list traversal to identify abnormal month-to-month consumption surges.
