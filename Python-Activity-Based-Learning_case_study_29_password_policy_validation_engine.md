# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Evaluate sample password strings against minimum length, character-category diversity, consecutive repetition, and prohibited-substring rules, reporting a clear explanation for every failed condition.

## 2. Objectives
- To inspect individual characters of a string using loops and conditional statements.
- To verify uppercase, lowercase, digit, and special character requirements.
- To detect prohibited substrings and consecutive repeated characters, reporting all failed rules.

## 3. Assumptions
- Minimum required password length is 8 characters.
- Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from '@#$%&*!'.
- No three identical characters may appear consecutively (e.g., 'aaa' or '111').
- Password must not contain prohibited substrings ('password', '1234', 'admin', 'qwerty') in any letter case.

## 4. Algorithm
1. Start the program.
2. Input password string pwd from the user.
3. Initialize boolean flags has_upper, has_lower, has_digit, has_special to False, has_triple to False, and an empty list errors.
4. Check if len(pwd) < 8; if so, add length failure message to errors.
5. Loop through each character ch in pwd to update uppercase, lowercase, digit, and special character flags.
6. Loop index i from 0 to len(pwd) - 3 to check if pwd[i] == pwd[i+1] == pwd[i+2]; if so, set has_triple = True.
7. Convert pwd to lowercase and check if any prohibited substring ('password', '1234', 'admin', 'qwerty') is present.
8. Append descriptive failure messages for every unmet rule to errors.
9. If errors is empty, print 'STRONG PASSWORD: All policy checks passed.'; otherwise print each error.
10. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
 / Input password string /
           |
           v
[ Check Length >= 8 ]
           |
           v
[ Loop chars: check Upper, Lower, Digit, Special ]
           |
           v
[ Loop index: check 3 consecutive identical chars ]
           |
           v
[ Check prohibited substrings (case-insensitive) ]
           |
           v
   < Any Errors ? > -- No --> [ Print VALID PASSWORD ]
           |                           |
          Yes                          v
           |                        [ End ]
           v
[ Print All Failed Rule Explanations ]
           |
           v
        [ End ]
```

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

    SET has_upper = FALSE, has_lower = FALSE, has_digit = FALSE, has_special = FALSE
    FOR EACH ch IN pwd DO
        IF ch >= 'A' AND ch <= 'Z' THEN SET has_upper = TRUE
        ELSE IF ch >= 'a' AND ch <= 'z' THEN SET has_lower = TRUE
        ELSE IF ch >= '0' AND ch <= '9' THEN SET has_digit = TRUE
        ELSE IF ch IN special_chars THEN SET has_special = TRUE
        ENDIF
    ENDFOR

    IF NOT has_upper THEN APPEND "Missing uppercase letter." TO errors
    IF NOT has_lower THEN APPEND "Missing lowercase letter." TO errors
    IF NOT has_digit THEN APPEND "Missing numeric digit." TO errors
    IF NOT has_special THEN APPEND "Missing special character." TO errors

    FOR i FROM 0 TO LENGTH(pwd) - 3 DO
        IF pwd[i] == pwd[i+1] AND pwd[i+1] == pwd[i+2] THEN
            APPEND "Contains 3 or more consecutive identical characters." TO errors
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
        FOR EACH err IN errors DO PRINT err ENDFOR
    ENDIF
END
```

## 7. Python Source Code
```python
# Case Study 29: Password Policy Validation Engine

pwd = input("Enter a password to validate: ")
errors = []

special_chars = "@#$%&*!"
prohibited_words = ["password", "1234", "admin", "qwerty"]

# 1. Minimum length check
if len(pwd) < 8:
    errors.append(f"Length rule failed: Password has {len(pwd)} characters (minimum 8 required).")

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

if not has_upper:
    errors.append("Character rule failed: Must contain at least one uppercase letter (A-Z).")
if not has_lower:
    errors.append("Character rule failed: Must contain at least one lowercase letter (a-z).")
if not has_digit:
    errors.append("Character rule failed: Must contain at least one digit (0-9).")
if not has_special:
    errors.append(f"Character rule failed: Must contain at least one special character ({special_chars}).")

# 3. Consecutive repetition check (3 or more identical characters in a row)
has_repetition = False
for i in range(len(pwd) - 2):
    if pwd[i] == pwd[i + 1] and pwd[i + 1] == pwd[i + 2]:
        has_repetition = True
        break

if has_repetition:
    errors.append("Repetition rule failed: Cannot contain 3 or more identical characters consecutively.")

# 4. Prohibited substring check
lower_pwd = pwd.lower()
for word in prohibited_words:
    if word in lower_pwd:
        errors.append(f"Prohibited substring rule failed: Contains forbidden sequence '{word}'.")

print("
--- Password Validation Report ---")
if len(errors) == 0:
    print("RESULT: VALID - Password satisfies all security policies.")
else:
    print(f"RESULT: INVALID - {len(errors)} rule(s) violated:")
    for idx in range(len(errors)):
        print(f"  {idx + 1}. {errors[idx]}")
```

## 8. Test Cases
- **Test Case 1 (Multiple Violations):** `admin111` -> Fails uppercase, special character, consecutive repetition (`111`), and prohibited substring (`admin`).
- **Test Case 2 (Valid Password):** `Campus@2026` -> Passes all checks.

## 9. Sample Output
```text
Enter a password to validate: admin111

--- Password Validation Report ---
RESULT: INVALID - 4 rule(s) violated:
  1. Character rule failed: Must contain at least one uppercase letter (A-Z).
  2. Character rule failed: Must contain at least one special character (@#$%&*!).
  3. Repetition rule failed: Cannot contain 3 or more identical characters consecutively.
  4. Prohibited substring rule failed: Contains forbidden sequence 'admin'.
```

## 10. Conclusion
The validation engine demonstrates character-level string inspection, substring membership testing, and detailed error aggregation using lists.
