# Case Study 35: Text Compression Using Character Runs

---

## 1. Problem Statement

The Text Compression Using Character Runs program compresses an input string using Run-Length Encoding (RLE). It groups consecutive repeated characters and represents each group using the character followed by its repetition count.

The program compares the lengths of the original and encoded strings to determine whether compression is beneficial, neutral, or results in increased size.

---

## 2. Objectives

- To traverse a string sequentially and identify consecutive repeated characters.
- To count the occurrences of identical characters in each run.
- To construct a compressed string using string concatenation.
- To compare the original and compressed string lengths.
- To calculate the percentage of space saved or expanded.
- To identify cases where compression is not beneficial.

---

## 3. Assumptions

| S.No. | Parameter | Assumption |
|---|---|---|
| 1 | Input String | Must be non-empty |
| 2 | Input Characters | Alphabetic characters only |
| 3 | Compression Method | Run-Length Encoding (RLE) |
| 4 | Encoding Format | Character followed by its repetition count |
| 5 | Example | `aaabb` becomes `a3b2` |
| 6 | Compression Benefit | Encoded length must be smaller than original length |
| 7 | Neutral Compression | Encoded length equals original length |
| 8 | Expansion | Encoded length is greater than original length |

---

## 4. Algorithm

1. Start the program.
2. Input a string from the user.
3. Check whether the input string is empty.
4. If the string is empty, display an error message and request input again.
5. Initialize an empty string named `encoded`.
6. Initialize a counter variable `count = 1`.
7. Traverse the input string starting from index 1.
8. Compare the current character with the previous character.
9. If both characters are identical:
   - Increment `count` by 1.
10. Otherwise:
    - Append the previous character and its count to `encoded`.
    - Reset `count = 1`.
11. After the loop, append the final character and its count.
12. Calculate the original string length and encoded string length.
13. Compare both lengths:
    - If encoded length is smaller, compression is beneficial.
    - If both lengths are equal, compression is neutral.
    - If encoded length is greater, compression is not beneficial.
14. Calculate the percentage of space saved or expanded.
15. Display the original string, encoded string, lengths, and compression status.
16. Stop the program.

---

## 5. Flowchart

```text id="c35flow"
              +----------------------+
              |        START         |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input String         |
              +----------------------+
                         |
                         v
                 +---------------+
                 | Is String     |
                 | Empty?        |
                 +---------------+
                   /          \
                 Yes           No
                  |             |
                  v             v
          +---------------+  +----------------------+
          | Display Error |  | encoded = ""         |
          | Re-enter Text |  | count = 1            |
          +---------------+  +----------------------+
                  |                    |
                  +-----> Input        v
                            +----------------------+
                            | Loop Through String  |
                            | Starting at Index 1  |
                            +----------------------+
                                       |
                                       v
                            +----------------------+
                            | Current Character == |
                            | Previous Character?  |
                            +----------------------+
                               /              \
                             Yes               No
                              |                 |
                              v                 v
                       +-------------+  +------------------+
                       | count += 1  |  | Append Previous  |
                       +-------------+  | Character + Count|
                              |          +------------------+
                              |                 |
                              |                 v
                              |          +-------------+
                              |          | count = 1   |
                              |          +-------------+
                              |                 |
                              +--------+--------+
                                       |
                                       v
                            +----------------------+
                            | Append Final         |
                            | Character + Count    |
                            +----------------------+
                                       |
                                       v
                            +----------------------+
                            | Compare String       |
                            | Lengths               |
                            +----------------------+
                                       |
                                       v
                            +----------------------+
                            | Display Compression  |
                            | Analysis Report       |
                            +----------------------+
                                       |
                                       v
                            +----------------------+
                            |         END          |
                            +----------------------+
```

---

## 6. Pseudocode

```text id="c35pseudo"
BEGIN

    READ text

    WHILE LENGTH(text) == 0 DO
        PRINT "Input cannot be empty."
        READ text
    ENDWHILE

    SET encoded = ""
    SET count = 1

    FOR i FROM 1 TO LENGTH(text) - 1 DO

        IF text[i] == text[i - 1] THEN

            SET count = count + 1

        ELSE

            SET encoded = encoded + text[i - 1] + STRING(count)
            SET count = 1

        ENDIF

    ENDFOR

    SET encoded = encoded + text[LENGTH(text) - 1] + STRING(count)

    SET orig_len = LENGTH(text)
    SET enc_len = LENGTH(encoded)

    PRINT "Original String:", text
    PRINT "Original Length:", orig_len

    PRINT "Encoded String:", encoded
    PRINT "Encoded Length:", enc_len

    IF enc_len < orig_len THEN

        SET savings = ((orig_len - enc_len) / orig_len) * 100
        PRINT "Compression Beneficial"
        PRINT "Space Saved:", savings

    ELSE IF enc_len == orig_len THEN

        PRINT "Compression Neutral"

    ELSE

        SET expansion = ((enc_len - orig_len) / orig_len) * 100
        PRINT "Compression Not Beneficial"
        PRINT "Size Expansion:", expansion

    ENDIF

END
```

---

## 7. Python Source Code

```python
# Case Study 35: Text Compression Using Character Runs

# 1. Input string
text = input("Enter a string to compress: ").strip()

while len(text) == 0:
    print("Input cannot be empty.")
    text = input("Re-enter a string to compress: ").strip()

# 2. Initialize variables
encoded = ""
count = 1

# 3. Run-Length Encoding
for i in range(1, len(text)):

    if text[i] == text[i - 1]:
        count += 1

    else:
        encoded += text[i - 1] + str(count)
        count = 1

# 4. Append the final character run
encoded += text[-1] + str(count)

# 5. Calculate string lengths
orig_len = len(text)
enc_len = len(encoded)

# 6. Display compression report
print("\n--- Run-Length Encoding (RLE) Analysis ---")

print(f"Original String : {text} (Length: {orig_len})")
print(f"Encoded String  : {encoded} (Length: {enc_len})")

# 7. Evaluate compression efficiency
if enc_len < orig_len:

    savings = ((orig_len - enc_len) / orig_len) * 100

    print(
        f"Status          : BENEFICIAL "
        f"(Saved {orig_len - enc_len} chars / {savings:.1f}%)"
    )

elif enc_len == orig_len:

    print("Status          : NEUTRAL (No size reduction achieved)")

else:

    expansion = ((enc_len - orig_len) / orig_len) * 100

    print(
        f"Status          : NOT BENEFICIAL "
        f"(Size increased by {enc_len - orig_len} chars / "
        f"{expansion:.1f}%)"
    )
```

---

## 8. Test Cases

| Test Case | Original String | Encoded String | Original Length | Encoded Length | Expected Result |
|---|---|---|---:|---:|---|
| 1 | `AAAAABBBCCDAA` | `A5B3C2D1A2` | 13 | 10 | Beneficial |
| 2 | `ABCDE` | `A1B1C1D1E1` | 5 | 10 | Not Beneficial |
| 3 | `AAAA` | `A4` | 4 | 2 | Beneficial |
| 4 | `AABBCC` | `A2B2C2` | 6 | 6 | Neutral |
| 5 | `AAAAAAAAAA` | `A10` | 10 | 3 | Beneficial |

### Compression Calculation

**Test Case 1 – High Repetition**

- Original String: `AAAAABBBCCDAA`
- Encoded String: `A5B3C2D1A2`
- Original Length: 13
- Encoded Length: 10

Percentage Saved:

\[
\frac{13-10}{13}\times100=23.1\%
\]

Result: **Beneficial**

**Test Case 2 – No Repetition**

- Original String: `ABCDE`
- Encoded String: `A1B1C1D1E1`
- Original Length: 5
- Encoded Length: 10

Percentage Expanded:

\[
\frac{10-5}{5}\times100=100\%
\]

Result: **Not Beneficial**

---

## 9. Sample Output

### Test Case 1: Compression Beneficial

**Input:**

```text
Enter a string to compress: AAAAABBBCCDAA
```

**Output:**

```text
--- Run-Length Encoding (RLE) Analysis ---
Original String : AAAAABBBCCDAA (Length: 13)
Encoded String  : A5B3C2D1A2 (Length: 10)
Status          : BENEFICIAL (Saved 3 chars / 23.1%)
```

### Test Case 2: Compression Not Beneficial

**Input:**

```text
Enter a string to compress: ABCDE
```

**Output:**

```text
--- Run-Length Encoding (RLE) Analysis ---
Original String : ABCDE (Length: 5)
Encoded String  : A1B1C1D1E1 (Length: 10)
Status          : NOT BENEFICIAL (Size increased by 5 chars / 100.0%)
```

---

## 10. Conclusion

The Text Compression Using Character Runs program demonstrates Run-Length Encoding (RLE) through sequential string traversal, character comparison, counting, and string concatenation.

It evaluates compression efficiency by comparing the original and encoded string lengths. The program shows that RLE is effective for highly repetitive data but may increase the size of strings containing fewer repeated characters.

This case study develops practical knowledge of string processing, loops, conditional statements, and basic compression techniques in Python.
