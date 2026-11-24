# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem Statement
Develop a Python program that simulates a sequence of ATM deposits and withdrawals on a bank account. The system must track the account balance, enforce per-transaction and daily withdrawal limits, reject invalid transactions (such as overdrafts or non-multiples of Rs. 100), and generate a final transaction summary.

## 2. Objectives
- To process a batch of deposit and withdrawal requests iteratively.
- To enforce banking constraints including minimum balance, denomination multiples, and daily withdrawal limits.
- To log accepted and rejected transactions in lists and display a complete audit summary.

## 3. Assumptions
- Initial account balance is Rs. 10,000.
- Minimum required balance to maintain in the account is Rs. 1,000.
- Maximum single withdrawal limit is Rs. 10,000, and total daily withdrawal limit is Rs. 25,000.
- All deposit and withdrawal amounts must be positive multiples of Rs. 100.
- Transaction types are entered as 'D' (Deposit) or 'W' (Withdrawal).

## 4. Algorithm
1. Start the program.
2. Initialize balance = 10000, daily_withdrawn = 0, total_deposited = 0, and an empty list logs.
3. Input the number of transactions n.
4. For each transaction i from 1 to n: input transaction type t_type and amount.
5. Check if amount <= 0 or amount % 100 != 0; if so, reject for invalid denomination.
6. If t_type is 'D', add amount to balance and total_deposited, and record in logs.
7. If t_type is 'W', validate against single limit (10000), daily limit (25000), and minimum balance (1000). If valid, deduct from balance and update daily_withdrawn; else reject with reason.
8. Display all logged transactions, total deposits, total withdrawals, and closing balance.
9. Stop the program.

## 5. Flowchart
```text
        [ Start ]
            |
            v
[ balance = 10000, daily_withdrawn = 0 ]
            |
            v
   / Input n transactions /
            |
            v
    < Loop i = 1 to n > ---- No ----> [ Print Summary & Final Balance ]
            |                                         |
           Yes                                        v
            |                                      [ End ]
            v
 / Input type (D/W) & amount /
            |
            v
 < amount > 0 and % 100 == 0 ? > -- No --> [ Log REJECTED ] --+
            |                                                 |
           Yes                                                |
            |                                                 |
            v                                                 |
    < type == 'D' ? > -- Yes --> [ balance += amount, Log ] --+
            |                                                 |
            No                                                |
            |                                                 |
            v                                                 |
 < Valid Withdrawal Limits & Min Bal? > - Yes -> [ balance -= amount, Log ]
            |                                                 |
            No --> [ Log REJECTED ] --------------------------+
                                                              |
            +-------------------------------------------------+
            |
            +------> (Next Iteration i + 1)
```

## 6. Pseudocode
```text
BEGIN
    SET balance = 10000
    SET daily_withdrawn = 0
    SET total_deposited = 0
    SET logs = []

    READ n
    FOR i FROM 1 TO n DO
        READ t_type, amount
        IF amount <= 0 OR amount MOD 100 != 0 THEN
            APPEND "Txn " + i + ": REJECTED - Invalid amount" TO logs
        ELSE IF t_type == "D" THEN
            SET balance = balance + amount
            SET total_deposited = total_deposited + amount
            APPEND "Txn " + i + ": ACCEPTED - Deposit Rs. " + amount TO logs
        ELSE IF t_type == "W" THEN
            IF amount > 10000 THEN
                APPEND "Txn " + i + ": REJECTED - Single limit exceeded" TO logs
            ELSE IF daily_withdrawn + amount > 25000 THEN
                APPEND "Txn " + i + ": REJECTED - Daily limit exceeded" TO logs
            ELSE IF balance - amount < 1000 THEN
                APPEND "Txn " + i + ": REJECTED - Minimum balance violation" TO logs
            ELSE
                SET balance = balance - amount
                SET daily_withdrawn = daily_withdrawn + amount
                APPEND "Txn " + i + ": ACCEPTED - Withdrawal Rs. " + amount TO logs
            ENDIF
        ELSE
            APPEND "Txn " + i + ": REJECTED - Unknown type" TO logs
        ENDIF
    ENDFOR

    FOR EACH entry IN logs DO
        PRINT entry
    ENDFOR
    PRINT total_deposited, daily_withdrawn, balance
END
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
- **Test Case 1 (Valid Deposit):** `D`, `5000` -> Accepted; balance updates from Rs. 10,000 to Rs. 15,000.
- **Test Case 2 (Invalid Denomination):** `W`, `250` -> Rejected; not a multiple of Rs. 100.
- **Test Case 3 (Single Limit Violation):** `W`, `12000` -> Rejected; exceeds single withdrawal limit of Rs. 10,000.
- **Test Case 4 (Valid Withdrawal):** `W`, `8000` -> Accepted; balance updates from Rs. 15,000 to Rs. 7,000.
- **Test Case 5 (Minimum Balance Violation):** `W`, `6500` -> Rejected; remaining balance Rs. 500 < Rs. 1,000.

## 9. Sample Output
```text
Initial Account Balance: Rs. 10000
Enter number of transactions to simulate: 5

Transaction 1:
Enter type (D for Deposit, W for Withdrawal): D
Enter amount (in multiples of 100): 5000
Txn 1 [ACCEPTED]: Deposited Rs. 5000 | Balance: Rs. 15000

Transaction 2:
Enter type (D for Deposit, W for Withdrawal): W
Enter amount (in multiples of 100): 250
Txn 2 [REJECTED]: Rs. 250 is not a positive multiple of 100.

Transaction 3:
Enter type (D for Deposit, W for Withdrawal): W
Enter amount (in multiples of 100): 12000
Txn 3 [REJECTED]: Rs. 12000 exceeds single limit of Rs. 10000.

Transaction 4:
Enter type (D for Deposit, W for Withdrawal): W
Enter amount (in multiples of 100): 8000
Txn 4 [ACCEPTED]: Withdrew Rs. 8000 | Balance: Rs. 7000

Transaction 5:
Enter type (D for Deposit, W for Withdrawal): W
Enter amount (in multiples of 100): 6500
Txn 5 [REJECTED]: Insufficient balance (Min Rs. 1000 required).

================ ATM TRANSACTION SUMMARY ================
Txn 1 [ACCEPTED]: Deposited Rs. 5000 | Balance: Rs. 15000
Txn 2 [REJECTED]: Rs. 250 is not a positive multiple of 100.
Txn 3 [REJECTED]: Rs. 12000 exceeds single limit of Rs. 10000.
Txn 4 [ACCEPTED]: Withdrew Rs. 8000 | Balance: Rs. 7000
Txn 5 [REJECTED]: Insufficient balance (Min Rs. 1000 required).
---------------------------------------------------------
Total Deposited : Rs. 5000
Total Withdrawn : Rs. 8000
Closing Balance : Rs. 7000
=========================================================
```

## 10. Conclusion
The ATM simulation accurately validates multi-layered banking constraints using nested conditionals and loops, maintains real-time account state, and preserves a transparent transaction log.
