Here is **Case Study 13: ATM Transaction Sequence Simulation** in the same GitHub README box-style format, with all 10 sections.

# CASE STUDY 13: ATM TRANSACTION SEQUENCE SIMULATION

---

## 1. PROBLEM STATEMENT

Develop a Python program that simulates a sequence of ATM deposits and withdrawals on a bank account. The system tracks account balance, enforces per-transaction and daily withdrawal limits, rejects invalid transactions such as overdrafts or non-multiples of Rs. 100, and generates a final transaction summary.

---

## 2. OBJECTIVES

- Process multiple deposit and withdrawal requests using loops.
- Enforce minimum balance requirements.
- Apply single and daily withdrawal limits.
- Validate transaction amounts and denominations.
- Store accepted and rejected transactions in a list.
- Generate a complete transaction audit summary.

---

## 3. ASSUMPTIONS

| Description                | Value                |
| -------------------------- | -------------------- |
| Initial Balance            | Rs. 10,000           |
| Minimum Balance            | Rs. 1,000            |
| Single Withdrawal Limit    | Rs. 10,000           |
| Daily Withdrawal Limit     | Rs. 25,000           |
| Minimum Transaction Amount | Rs. 100              |
| Valid Denomination         | Multiples of Rs. 100 |
| Deposit Type               | D                    |
| Withdrawal Type            | W                    |

---

## 4. ALGORITHM

1. Start the program.
2. Initialize account balance to Rs. 10,000.
3. Initialize daily withdrawal and total deposit amounts to zero.
4. Create an empty transaction log list.
5. Input the number of transactions.
6. Repeat for each transaction:
   - Input transaction type (D/W).
   - Input transaction amount.
   - Check whether the amount is positive and a multiple of Rs. 100.
   - If the type is D, deposit the amount and update the balance.
   - If the type is W, check the single withdrawal limit.
   - Check the daily withdrawal limit.
   - Check the minimum balance requirement.
   - Accept or reject the transaction with an appropriate reason.
   - Store the transaction result in the log.
7. Display all transaction records.
8. Display total deposits, total withdrawals, and closing balance.
9. Stop the program.

---

## 5. FLOWCHART

```
             +----------------+
             |     START      |
             +----------------+
                     |
                     v
       +----------------------------+
       | Initialize Balance = 10000 |
       | Daily Withdrawn = 0        |
       | Total Deposited = 0        |
       | Logs = []                  |
       +----------------------------+
                     |
                     v
       +----------------------------+
       | Input Number of            |
       | Transactions (n)           |
       +----------------------------+
                     |
                     v
             +---------------+
             | More          |
             | Transactions?|
             +---------------+
                |        |
               Yes       No
                |        |
                v        v
       +----------------+  +------------------+
       | Input Type and |  | Display Final    |
       | Amount         |  | Transaction      |
       +----------------+  | Summary          |
                |          +------------------+
                v                   |
       +-------------------+        v
       | Amount > 0 and    |      +-------+
       | Amount % 100 = 0? |      |  END  |
       +-------------------+      +-------+
           |          |
          No         Yes
           |          |
           v          v
       +---------+  +-------------+
       | Reject  |  | Type = D ?  |
       | Invalid |  +-------------+
       | Amount  |     |       |
       +---------+    Yes      No
           |           |       |
           |           v       v
           |    +----------+  +----------------+
           |    | Deposit  |  | Type = W ?     |
           |    | Update   |  +----------------+
           |    | Balance  |      |       |
           |    +----------+     Yes      No
           |         |             |       |
           |         |             v       v
           |         |     +------------+ +---------+
           |         |     | Check      | | Reject  |
           |         |     | Withdrawal | | Unknown |
           |         |     | Limits     | | Type    |
           |         |     +------------+ +---------+
           |         |             |
           |         |             v
           |         |     +----------------+
           |         |     | All Limits    |
           |         |     | Satisfied?     |
           |         |     +----------------+
           |         |       |         |
           |         |      Yes        No
           |         |       |         |
           |         |       v         v
           |         |   +---------+ +---------+
           |         |   | Accept  | | Reject  |
           |         |   | Withdraw| | With    |
           |         |   | Update  | | Reason  |
           |         |   | Balance | |         |
           |         |   +---------+ +---------+
           |         |       |         |
           +---------+-------+---------+
                     |
                     v
             +----------------+
             | Store Result   |
             | in Logs        |
             +----------------+
                     |
                     +------> Next Transaction
```

---

## 6. PSEUDOCODE

```
BEGIN

    SET balance = 10000
    SET min_balance = 1000
    SET single_limit = 10000
    SET daily_limit = 25000

    SET daily_withdrawn = 0
    SET total_deposited = 0
    SET logs = []

    READ n

    FOR i FROM 1 TO n DO

        READ t_type, amount

        IF amount <= 0 OR amount MOD 100 != 0 THEN

            APPEND "REJECTED - Invalid amount" TO logs

        ELSE IF t_type == "D" THEN

            balance = balance + amount
            total_deposited = total_deposited + amount

            APPEND "ACCEPTED - Deposit" TO logs

        ELSE IF t_type == "W" THEN

            IF amount > single_limit THEN

                APPEND "REJECTED - Single limit exceeded" TO logs

            ELSE IF daily_withdrawn + amount > daily_limit THEN

                APPEND "REJECTED - Daily limit exceeded" TO logs

            ELSE IF balance - amount < min_balance THEN

                APPEND "REJECTED - Minimum balance violation" TO logs

            ELSE

                balance = balance - amount
                daily_withdrawn = daily_withdrawn + amount

                APPEND "ACCEPTED - Withdrawal" TO logs

            ENDIF

        ELSE

            APPEND "REJECTED - Unknown transaction type" TO logs

        ENDIF

    ENDFOR

    FOR EACH entry IN logs DO
        DISPLAY entry
    ENDFOR

    DISPLAY total_deposited
    DISPLAY daily_withdrawn
    DISPLAY balance

END
```

---

## 7. PYTHON SOURCE CODE

```
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

while n <= 0:
    print("Invalid input. Enter at least one transaction.")
    n = int(input("Re-enter number of transactions: "))

for i in range(1, n + 1):

    print(f"\\nTransaction {i}:")

    t_type = input(
        "Enter type (D for Deposit, W for Withdrawal): "
    ).strip().upper()

    amount = int(input("Enter amount (in multiples of 100): "))

    # Validate transaction amount
    if amount <= 0 or amount % 100 != 0:

        status = (
            f"Txn {i} [REJECTED]: Rs. {amount} "
            "is not a positive multiple of 100."
        )

    # Deposit transaction
    elif t_type == "D":

        balance += amount
        total_deposited += amount

        status = (
            f"Txn {i} [ACCEPTED]: Deposited Rs. {amount} "
            f"| Balance: Rs. {balance}"
        )

    # Withdrawal transaction
    elif t_type == "W":

        if amount > single_limit:

            status = (
                f"Txn {i} [REJECTED]: Rs. {amount} "
                f"exceeds single limit of Rs. {single_limit}."
            )

        elif daily_withdrawn + amount > daily_limit:

            status = (
                f"Txn {i} [REJECTED]: Rs. {amount} "
                f"exceeds daily limit of Rs. {daily_limit}."
            )

        elif balance - amount < min_balance:

            status = (
                f"Txn {i} [REJECTED]: Insufficient balance "
                f"(Min Rs. {min_balance} required)."
            )

        else:

            balance -= amount
            daily_withdrawn += amount

            status = (
                f"Txn {i} [ACCEPTED]: Withdrew Rs. {amount} "
                f"| Balance: Rs. {balance}"
            )

    # Invalid transaction type
    else:

        status = (
            f"Txn {i} [REJECTED]: "
            f"Invalid transaction type '{t_type}'."
        )

    logs.append(status)
    print(status)


# Display final transaction summary
print("\\n================ ATM TRANSACTION SUMMARY ================")

for entry in logs:
    print(entry)

print("---------------------------------------------------------")
print(f"Total Deposited : Rs. {total_deposited}")
print(f"Total Withdrawn : Rs. {daily_withdrawn}")
print(f"Closing Balance : Rs. {balance}")
print("=========================================================")
```

---

## 8. TEST CASES

| Test Case                 | Transaction   | Expected Result |
| ------------------------- | ------------- | --------------- |
| Valid Deposit             | D, Rs. 5,000  | Accepted        |
| Invalid Denomination      | W, Rs. 250    | Rejected        |
| Single Limit Violation    | W, Rs. 12,000 | Rejected        |
| Valid Withdrawal          | W, Rs. 8,000  | Accepted        |
| Minimum Balance Violation | W, Rs. 6,500  | Rejected        |

### Test Case Calculations

**Test Case 1: Valid Deposit**

- Initial Balance = Rs. 10,000
- Deposit = Rs. 5,000
- New Balance = **Rs. 15,000**

**Test Case 2: Invalid Denomination**

- Withdrawal = Rs. 250
- Rs. 250 is not a multiple of Rs. 100.
- Result = **REJECTED**

**Test Case 3: Single Limit Violation**

- Withdrawal = Rs. 12,000
- Maximum single withdrawal = Rs. 10,000.
- Result = **REJECTED**

**Test Case 4: Valid Withdrawal**

- Current Balance = Rs. 15,000
- Withdrawal = Rs. 8,000
- New Balance = **Rs. 7,000**

**Test Case 5: Minimum Balance Violation**

- Current Balance = Rs. 7,000
- Withdrawal = Rs. 6,500
- Remaining Balance = Rs. 500
- Minimum Balance = Rs. 1,000
- Result = **REJECTED**

---

## 9. SAMPLE OUTPUT

```
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

---

## 10. CONCLUSION

The ATM Transaction Sequence Simulation successfully processes deposits and withdrawals while enforcing multiple banking constraints. It uses loops, conditional statements, and lists to validate transactions, maintain account balance, track accepted and rejected requests, and generate a complete transaction summary.

---

**END OF CASE STUDY 13**

Add rejected transaction trackingFix escaped newline formatting
