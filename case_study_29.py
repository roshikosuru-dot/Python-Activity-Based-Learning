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
