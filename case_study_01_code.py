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
