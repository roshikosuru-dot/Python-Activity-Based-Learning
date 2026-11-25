# Case Study 13: ATM Transaction Sequence Simulation

balance = 10000
min_balance = 1000
single_limit = 10000
daily_limit = 25000

daily_withdrawn = 0
total_deposited = 0
logs = []

print(f"Initial Account Balance: Rs. {balance}")
n = int(input("Enter number of transactions to simulate: "))

for i in range(1, n + 1):
    print(f"\nTransaction {i}:")
    t_type = input("Enter type (D for Deposit, W for Withdrawal): ").strip().upper()
    amount = int(input("Enter amount (in multiples of 100): "))

    if amount <= 0 or amount % 100 != 0:
        status = f"Txn {i} [REJECTED]: Rs. {amount} is not a positive multiple of 100."
        logs.append(status)
        print(status)
    elif t_type == "D":
        balance += amount
        total_deposited += amount
        status = f"Txn {i} [ACCEPTED]: Deposited Rs. {amount} | Balance: Rs. {balance}"
        logs.append(status)
        print(status)
    elif t_type == "W":
        if amount > single_limit:
            status = f"Txn {i} [REJECTED]: Rs. {amount} exceeds single limit of Rs. {single_limit}."
        elif daily_withdrawn + amount > daily_limit:
            status = f"Txn {i} [REJECTED]: Rs. {amount} exceeds daily limit of Rs. {daily_limit}."
        elif balance - amount < min_balance:
            status = f"Txn {i} [REJECTED]: Insufficient balance (Min Rs. {min_balance} required)."
        else:
            balance -= amount
            daily_withdrawn += amount
            status = f"Txn {i} [ACCEPTED]: Withdrew Rs. {amount} | Balance: Rs. {balance}"
        logs.append(status)
        print(status)
    else:
        status = f"Txn {i} [REJECTED]: Invalid transaction type '{t_type}'."
        logs.append(status)
        print(status)

print("\n================ ATM TRANSACTION SUMMARY ================")
for entry in logs:
    print(entry)
print("---------------------------------------------------------")
print(f"Total Deposited : Rs. {total_deposited}")
print(f"Total Withdrawn : Rs. {daily_withdrawn}")
print(f"Closing Balance : Rs. {balance}")
print("=========================================================")
