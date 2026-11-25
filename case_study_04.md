# Case Study 29: Password Policy Validation Engine

---

## 1. Problem Statement

The Password Policy Validation Engine evaluates password strings against predefined security rules. It checks minimum length, character-category diversity, consecutive character repetition, and prohibited substrings.

The program reports every failed condition with a clear explanation. If all conditions are satisfied, the password is accepted.

---

## 2. Objectives

- To inspect individual characters of a string using loops and conditional statements.
- To verify uppercase, lowercase, digit, and special character requirements.
- To check the minimum password length.
- To detect three or more identical consecutive characters.
- To identify prohibited substrings without considering letter case.
- To display all validation errors instead of stopping at the first failure.

---

## 3. Assumptions

| S.No. | Validation Rule | Requirement |
|---|---|---|
| 1 | Minimum Length | At least 8 characters |
| 2 | Uppercase | At least one uppercase letter (A–Z) |
| 3 | Lowercase | At least one lowercase letter (a–z) |
| 4 | Numeric Digit | At least one digit (0–9) |
| 5 | Special Character | At least one character from `@#$%&*!` |
| 6 | Consecutive Repetition | No three identical consecutive characters |
| 7 | Prohibited Substrings | Must not contain `password`, `1234`, `admin`, or `qwerty` |
| 8 | Case Sensitivity | Prohibited substring checking is case-insensitive |

---

## 4. Algorithm

1. Start the program.
2. Read the password string from the user.
3. Initialize an empty list named `errors`.
4. Define the allowed special characters and prohibited substrings.
5. Check whether the password contains at least 8 characters.
6. Initialize four Boolean flags:
   - `has_upper`
   - `has_lower`
   - `has_digit`
   - `has_special`
7. Traverse each character in the password using a loop.
8. Update the corresponding flags based on the character category.
9. Add an error message for every missing character category.
10. Traverse the password using an index-based loop to detect three identical consecutive characters.
11. Convert the password into lowercase.
12. Check whether any prohibited substring exists in the password.
13. Add an error message for every prohibited substring found.
14. Check whether the `errors` list is empty.
15. If empty, display the password acceptance message.
16. Otherwise, display the number of failed rules and all error messages.
17. Stop the program.

---

## 5. Flowchart

```text
              +----------------+
              |     START      |
              +----------------+
                      |
                      v
              +----------------+
              | Input Password |
              +----------------+
                      |
                      v
              +----------------+
              | Check Length   |
              | Minimum 8      |
              +----------------+
                      |
                      v
              +----------------+
              | Check Upper,   |
              | Lower, Digit,  |
              | Special Char   |
              +----------------+
                      |
                      v
              +----------------+
              | Check Three    |
              | Identical      |
              | Consecutive    |
              | Characters     |
              +----------------+
                      |
                      v
              +----------------+
              | Check Prohibited|
              | Substrings     |
              +----------------+
                      |
                      v
                +------------+
                | Any Errors?|
                +------------+
                  /        \
                Yes         No
                 |           |
                 v           v
        +----------------+  +----------------+
        | Print All      |  | Print Password |
        | Failed Rules   |  | Accepted       |
        +----------------+  +----------------+
                 |                 |
                 v                 v
              +----------------------+
              |         END          |
              +----------------------+
```

---

## 6. Pseudocode

```text
BEGIN

    READ pwd

    SET errors = []
    SET special_chars = "@#$%&*!"
    SET banned = ["password", "1234", "admin", "qwerty"]

    IF LENGTH(pwd) < 8 THEN
        APPEND "Minimum length of 8 characters required." TO errors
    ENDIF

    SET has_upper = FALSE
    SET has_lower = FALSE
    SET has_digit = FALSE
    SET has_special = FALSE

    FOR EACH ch IN pwd DO

        IF ch >= 'A' AND ch <= 'Z' THEN
            SET has_upper = TRUE

        ELSE IF ch >= 'a' AND ch <= 'z' THEN
            SET has_lower = TRUE

        ELSE IF ch >= '0' AND ch <= '9' THEN
            SET has_digit = TRUE

        ELSE IF ch IN special_chars THEN
            SET has_special = TRUE

        ENDIF

    ENDFOR

    IF NOT has_upper THEN
        APPEND "Missing uppercase letter." TO errors
    ENDIF

    IF NOT has_lower THEN
        APPEND "Missing lowercase letter." TO errors
    ENDIF

    IF NOT has_digit THEN
        APPEND "Missing numeric digit." TO errors
    ENDIF

    IF NOT has_special THEN
        APPEND "Missing special character." TO errors
    ENDIF

    FOR i FROM 0 TO LENGTH(pwd) - 3 DO

        IF pwd[i] == pwd[i+1] AND pwd[i+1] == pwd[i+2] THEN

            APPEND "Contains three consecutive identical characters." TO errors
            BREAK

        ENDIF

    ENDFOR

    SET lower_pwd = LOWERCASE(pwd)

    FOR EACH word IN banned DO

        IF word IN lower_pwd THEN
            APPEND "Contains prohibited substring: " + word TO errors
        ENDIF

    ENDFOR

    IF LENGTH(errors) == 0 THEN

        PRINT "Password ACCEPTED."

    ELSE

        PRINT "Password REJECTED:"

        FOR EACH err IN errors DO
            PRINT err
        ENDFOR

    ENDIF

END
```

---

## 7. Python Source Code

```python
# Case Study 29: Password Policy Validation Engine

pwd = input("Enter a password to validate: ")
errors = []

special_chars = "@#$%&*!"
prohibited_words = ["password", "1234", "admin", "qwerty"]

# 1. Minimum length check
if len(pwd) < 8:
    errors.append(
        f"Length rule failed: Password has {len(pwd)} "
        "(minimum 8 required)."
    )

# 2. Character category checks
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in pwd:
    if "A" <= ch <= "Z":
        has_upper = True

    elif "a" <= ch <= "z":
        has_lower = True

    elif "0" <= ch <= "9":
        has_digit = True

    elif ch in special_chars:
        has_special = True

# Report missing character categories
if not has_upper:
    errors.append(
        "Character rule failed: Must contain at least "
        "one uppercase letter (A-Z)."
    )

if not has_lower:
    errors.append(
        "Character rule failed: Must contain at least "
        "one lowercase letter (a-z)."
    )

if not has_digit:
    errors.append(
        "Character rule failed: Must contain at least "
        "one digit (0-9)."
    )

if not has_special:
    errors.append(
        f"Character rule failed: Must contain at least "
        f"one special character ({special_chars})."
    )

# 3. Consecutive repetition check
has_repetition = False

for i in range(len(pwd) - 2):
    if pwd[i] == pwd[i + 1] == pwd[i + 2]:
        has_repetition = True
        break

if has_repetition:
    errors.append(
        "Repetition rule failed: Cannot contain 3 or more "
        "identical characters consecutively."
    )

# 4. Prohibited substring check
lower_pwd = pwd.lower()

for word in prohibited_words:
    if word in lower_pwd:
        errors.append(
            f"Prohibited substring rule failed: "
            f"Contains forbidden sequence '{word}'."
        )

# 5. Display validation report
print("\n--- Password Validation Report ---")

if len(errors) == 0:
    print("RESULT: VALID - Password satisfies all security policies.")

else:
    print(f"RESULT: INVALID - {len(errors)} rule(s) violated:")

    for idx, error in enumerate(errors, start=1):
        print(f"  {idx}. {error}")
```

---

## 8. Test Cases

| Test Case | Input Password | Expected Result | Reason |
|---|---|---|---|
| 1 | `admin111` | Invalid | Missing uppercase and special character; contains `111` and prohibited substring `admin` |
| 2 | `Campus@2026` | Valid | Satisfies all validation rules |
| 3 | `abc12345` | Invalid | Missing uppercase and special character |
| 4 | `ABC@1234` | Invalid | Missing lowercase and contains prohibited substring `1234` |
| 5 | `Campus@@@2026` | Invalid | Contains three consecutive identical characters |
| 6 | `Pass@word1` | Invalid | Contains prohibited substring `password` (case-insensitive) |

---

## 9. Sample Output

### Test Case 1: Invalid Password

**Input:**

```text
Enter a password to validate: admin111
```

**Output:**

```text
--- Password Validation Report ---
RESULT: INVALID - 4 rule(s) violated:
  1. Character rule failed: Must contain at least one uppercase letter (A-Z).
  2. Character rule failed: Must contain at least one special character (@#$%&*!).
  3. Repetition rule failed: Cannot contain 3 or more identical characters consecutively.
  4. Prohibited substring rule failed: Contains forbidden sequence 'admin'.
```

### Test Case 2: Valid Password

**Input:**

```text
Enter a password to validate: Campus@2026
```

**Output:**

```text
--- Password Validation Report ---
RESULT: VALID - Password satisfies all security policies.
```

---

## 10. Conclusion

The Password Policy Validation Engine demonstrates effective string manipulation, character inspection, loops, conditional statements, and substring searching in Python.

The program checks multiple password rules and collects all validation errors in a list. It provides clear feedback for every failed condition and accepts passwords only when all specified policies are satisfied.

This case study helps develop practical knowledge of string processing, Boolean flags, list operations, and decision-making in Python.
