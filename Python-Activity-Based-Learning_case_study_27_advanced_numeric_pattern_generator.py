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
