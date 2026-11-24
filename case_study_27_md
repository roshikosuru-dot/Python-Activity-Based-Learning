# Case Study 27: Advanced Numeric Pattern Generator

## 1. Problem Statement
Design a Python program to produce a symmetric hollow numeric diamond pattern based on a user-specified dimension n, including input validation for invalid dimensions and carefully aligned spacing.

## 2. Objectives
- To validate user-supplied pattern dimensions within a valid range.
- To generate a symmetric hollow numeric diamond using nested loops and conditional boundary checks.
- To ensure clean horizontal and vertical alignment of numbers and spaces.

## 3. Assumptions
- The dimension n represents the row number of the widest middle row (half-height).
- Valid dimensions are integers between 2 and 9 so single-digit numbers preserve exact column alignment.
- The upper half runs from row 1 to n, and the lower half mirrors from row n - 1 down to 1.

## 4. Algorithm
1. Start the program.
2. Read integer dimension n from the user.
3. Validate that 2 <= n <= 9; if invalid, display an error message and prompt again.
4. For the upper half (row i from 1 to n): print (n - i) leading spaces, then print i. If i > 1, print (2 * i - 3) inner spaces followed by i.
5. For the lower half (row i from n - 1 down to 1): print (n - i) leading spaces, then print i. If i > 1, print (2 * i - 3) inner spaces followed by i.
6. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
  / Input dimension n /
           |
           v
  < 2 <= n <= 9 ? > -- No --> [ Print Error & Re-input ]
           |
          Yes
           |
           v
[ Loop i = 1 to n (Upper Half) ]
           |
           v
[ Print leading spaces, i, inner spaces, i (if i > 1) ]
           |
           v
[ Loop i = n-1 down to 1 (Lower Half) ]
           |
           v
[ Print leading spaces, i, inner spaces, i (if i > 1) ]
           |
           v
        [ End ]
```

## 6. Pseudocode
```text
BEGIN
    READ n
    WHILE n < 2 OR n > 9 DO
        PRINT "Invalid dimension. Enter a number between 2 and 9."
        READ n
    ENDWHILE

    FOR i FROM 1 TO n DO
        PRINT " " * (n - i) + STRING(i)
        IF i > 1 THEN
            PRINT " " * (2 * i - 3) + STRING(i)
        ENDIF
        PRINT NEWLINE
    ENDFOR

    FOR i FROM n - 1 DOWN TO 1 DO
        PRINT " " * (n - i) + STRING(i)
        IF i > 1 THEN
            PRINT " " * (2 * i - 3) + STRING(i)
        ENDIF
        PRINT NEWLINE
    ENDFOR
END
```

## 7. Python Source Code
```python
# Case Study 27: Advanced Numeric Pattern Generator

n = int(input("Enter diamond half-height dimension (2 to 9): "))
while n < 2 or n > 9:
    print("Invalid dimension! Please enter an integer between 2 and 9.")
    n = int(input("Re-enter dimension (2 to 9): "))

print(f"\n--- Hollow Numeric Diamond (n = {n}) ---\n")

# Upper half including middle row
for i in range(1, n + 1):
    # Leading spaces
    for s in range(n - i):
        print(" ", end="")
    # First boundary digit
    print(i, end="")
    # Inner spaces and second boundary digit
    if i > 1:
        for s in range(2 * i - 3):
            print(" ", end="")
        print(i, end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    # Leading spaces
    for s in range(n - i):
        print(" ", end="")
    # First boundary digit
    print(i, end="")
    # Inner spaces and second boundary digit
    if i > 1:
        for s in range(2 * i - 3):
            print(" ", end="")
        print(i, end="")
    print()
```

## 8. Test Cases
- **Test Case 1 (Invalid Input):** `n = 1` or `n = 12` -> Rejected with validation prompt until valid input is entered.
- **Test Case 2 (Valid Input n = 5):** Produces a 9-row symmetric hollow diamond peaking at `5       5`.

## 9. Sample Output
```text
Enter diamond half-height dimension (2 to 9): 5

--- Hollow Numeric Diamond (n = 5) ---

    1
   2 2
  3   3
 4     4
5       5
 4     4
  3   3
   2 2
    1
```

## 10. Conclusion
Using nested loops and boundary space calculations, the program validates user dimensions and renders a symmetrical, properly aligned hollow numeric diamond.
