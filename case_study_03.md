# CASE STUDY 27: ADVANCED NUMERIC PATTERN GENERATOR

---

## 1. PROBLEM STATEMENT

Design and implement a Python program to generate a symmetric hollow numeric diamond pattern based on a user-specified dimension `n`. The program validates the input dimension and uses nested loops and spacing calculations to produce a properly aligned diamond pattern.

---

## 2. OBJECTIVES

- Validate user-supplied pattern dimensions within a specified range.
- Generate a symmetric hollow numeric diamond using nested loops.
- Apply conditional statements to print boundary numbers.
- Calculate leading and inner spaces for proper alignment.
- Display the upper and lower halves of the diamond symmetrically.

---

## 3. ASSUMPTIONS

| Description | Value |
|:---|:---|
| Minimum Dimension | 2 |
| Maximum Dimension | 9 |
| Input Type | Integer |
| Pattern Type | Hollow Numeric Diamond |
| Upper Half | Row 1 to n |
| Lower Half | Row n-1 to 1 |
| Total Rows | 2n - 1 |

---

## 4. ALGORITHM

1. Start the program.
2. Read the diamond half-height dimension `n`.
3. Validate that `n` is between 2 and 9.
4. If the input is invalid, display an error message and request input again.
5. Generate the upper half:
   - Iterate from row 1 to row n.
   - Print leading spaces based on the current row.
   - Print the first boundary number.
   - If the row is greater than 1, print inner spaces and the second boundary number.
6. Generate the lower half:
   - Iterate from row n-1 down to row 1.
   - Print leading spaces.
   - Print the first boundary number.
   - If the row is greater than 1, print inner spaces and the second boundary number.
7. Stop the program.

---

## 5. FLOWCHART

```text
             +----------------+
             |     START      |
             +----------------+
                     |
                     v
          +----------------------+
          | Input Dimension n    |
          +----------------------+
                     |
                     v
             +---------------+
             | 2 <= n <= 9 ? |
             +---------------+
                |        |
               No       Yes
                |        |
                v        v
        +-------------+  +------------------+
        | Display     |  | Generate Upper   |
        | Error       |  | Half (1 to n)    |
        +-------------+  +------------------+
                |                  |
                +-- Re-enter       v
                         +------------------+
                         | Print Leading    |
                         | Spaces and Digit |
                         +------------------+
                                    |
                                    v
                         +------------------+
                         | Print Inner      |
                         | Spaces and Digit |
                         +------------------+
                                    |
                                    v
                         +------------------+
                         | Generate Lower   |
                         | Half (n-1 to 1)   |
                         +------------------+
                                    |
                                    v
                         +------------------+
                         | Print Leading    |
                         | and Inner Spaces |
                         +------------------+
                                    |
                                    v
                            +---------------+
                            |      END      |
                            +---------------+
```

---

## 6. PSEUDOCODE

```text
BEGIN

    READ n

    WHILE n < 2 OR n > 9 DO
        PRINT "Invalid dimension"
        READ n
    ENDWHILE

    PRINT "Hollow Numeric Diamond"

    FOR i FROM 1 TO n DO

        PRINT " " * (n - i)
        PRINT i

        IF i > 1 THEN
            PRINT " " * (2 * i - 3)
            PRINT i
        ENDIF

        PRINT NEWLINE

    ENDFOR

    FOR i FROM n - 1 DOWN TO 1 DO

        PRINT " " * (n - i)
        PRINT i

        IF i > 1 THEN
            PRINT " " * (2 * i - 3)
            PRINT i
        ENDIF

        PRINT NEWLINE

    ENDFOR

END
```

---

## 7. PYTHON SOURCE CODE

```python
# Case Study 27: Advanced Numeric Pattern Generator

n = int(input("Enter diamond half-height dimension (2 to 9): "))

# Validate the input dimension
while n < 2 or n > 9:
    print("Invalid dimension! Please enter an integer between 2 and 9.")
    n = int(input("Re-enter dimension (2 to 9): "))

print(f"\\n--- Hollow Numeric Diamond (n = {n}) ---\\n")

# Upper half including middle row
for i in range(1, n + 1):

    # Print leading spaces
    for s in range(n - i):
        print(" ", end="")

    # Print first boundary digit
    print(i, end="")

    # Print inner spaces and second boundary digit
    if i > 1:
        for s in range(2 * i - 3):
            print(" ", end="")

        print(i, end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    # Print leading spaces
    for s in range(n - i):
        print(" ", end="")

    # Print first boundary digit
    print(i, end="")

    # Print inner spaces and second boundary digit
    if i > 1:
        for s in range(2 * i - 3):
            print(" ", end="")

        print(i, end="")

    print()
```

---

## 8. TEST CASES

| Test Case | Input | Expected Result |
|:---|:---:|:---|
| Invalid Minimum | 1 | Rejected |
| Invalid Maximum | 12 | Rejected |
| Valid Minimum | 2 | 3-row hollow diamond |
| Valid Input | 5 | 9-row hollow diamond |
| Valid Maximum | 9 | 17-row hollow diamond |

### Test Case 1: Invalid Input

- Input = 1
- Minimum allowed value = 2
- Result = **Invalid dimension**

### Test Case 2: Valid Input (n = 5)

- Upper half = 5 rows
- Lower half = 4 rows
- Total rows = 9
- Result = **Symmetric Hollow Numeric Diamond**

---

## 9. SAMPLE OUTPUT

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

---

## 10. CONCLUSION

The Advanced Numeric Pattern Generator successfully generates a symmetric hollow numeric diamond using nested loops, conditional statements, and spacing calculations. It validates user input and ensures proper horizontal and vertical alignment of the generated pattern.

---

**END OF CASE STUDY 27**
