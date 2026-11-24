# Case Study 35: Text Compression Using Character Runs

## 1. Problem Statement
Encode an input string using Run-Length Encoding (RLE) by grouping consecutive repeated characters and compare the original and encoded string lengths, identifying cases where compression is not beneficial.

## 2. Objectives
- To traverse a string sequentially and count consecutive identical characters.
- To construct a compressed string representation using string concatenation.
- To evaluate compression efficiency and detect expansion cases where the encoded string is longer than or equal to the original.

## 3. Assumptions
- Input string is non-empty and consists of alphabetic characters (no embedded digits that could cause ambiguity).
- Each consecutive run of character c of length k is encoded as c followed by str(k) (e.g., 'aaabb' -> 'a3b2').
- Compression is considered beneficial only if len(encoded) < len(original).

## 4. Algorithm
1. Start the program.
2. Input non-empty string text from the user.
3. Initialize encoded = '' and count = 1.
4. Loop index i from 1 to len(text) - 1:
5.   If text[i] == text[i - 1], increment count by 1.
6.   Else append text[i - 1] + str(count) to encoded and reset count = 1.
7. After the loop ends, append text[-1] + str(count) to encoded.
8. Compare len(encoded) with len(text) and compute space saved or expanded percentage.
9. Display original string, encoded string, lengths, and whether compression was beneficial.
10. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
  / Input string text /
           |
           v
[ encoded = "", count = 1 ]
           |
           v
 < Loop i = 1 to len(text)-1 > -- No --> [ Append text[-1] + str(count) ]
           |                                             |
          Yes                                            v
           |                                   [ Compare Lengths ]
           v                                             |
< text[i] == text[i-1] ? >                               v
      /          \                           / Print Compression Report /
    Yes           No                                     |
    /              \                                     v
[ count += 1 ]  [ encoded += text[i-1]+str(count) ]   [ End ]
                [ count = 1 ]
```

## 6. Pseudocode
```text
BEGIN
    READ text
    IF LENGTH(text) == 0 THEN
        PRINT "Empty string."
        STOP
    ENDIF

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

    PRINT text, LENGTH(text)
    PRINT encoded, LENGTH(encoded)
    IF LENGTH(encoded) < LENGTH(text) THEN
        PRINT "Compression Beneficial"
    ELSE
        PRINT "Compression Not Beneficial"
    ENDIF
END
```

## 7. Python Source Code
```python
# Case Study 35: Text Compression Using Character Runs

text = input("Enter a string to compress: ").strip()
while len(text) == 0:
    print("Input cannot be empty.")
    text = input("Re-enter a string to compress: ").strip()

encoded = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encoded += text[i - 1] + str(count)
        count = 1

# Append the final character run
encoded += text[-1] + str(count)

orig_len = len(text)
enc_len = len(encoded)

print("
--- Run-Length Encoding (RLE) Analysis ---")
print(f"Original String : {text} (Length: {orig_len})")
print(f"Encoded String  : {encoded} (Length: {enc_len})")

if enc_len < orig_len:
    savings = ((orig_len - enc_len) / orig_len) * 100
    print(f"Status          : BENEFICIAL (Saved {orig_len - enc_len} chars / {savings:.1f}%)")
elif enc_len == orig_len:
    print("Status          : NEUTRAL (No size reduction achieved)")
else:
    expansion = ((enc_len - orig_len) / orig_len) * 100
    print(f"Status          : NOT BENEFICIAL (Size increased by {enc_len - orig_len} chars / {expansion:.1f}%)")
```

## 8. Test Cases
- **Test Case 1 (High Repetition - Beneficial):** `AAAAABBBCCDAA` (len 13) -> `A5B3C2D1A2` (len 10) -> **Beneficial** (23.1% reduction).
- **Test Case 2 (No Repetition - Not Beneficial):** `ABCDE` (len 5) -> `A1B1C1D1E1` (len 10) -> **Not Beneficial** (100% size expansion).

## 9. Sample Output
```text
Enter a string to compress: AAAAABBBCCDAA

--- Run-Length Encoding (RLE) Analysis ---
Original String : AAAAABBBCCDAA (Length: 13)
Encoded String  : A5B3C2D1A2 (Length: 10)
Status          : BENEFICIAL (Saved 3 chars / 23.1%)
```

## 10. Conclusion
The character-run compression algorithm accurately encodes consecutive runs and demonstrates why Run-Length Encoding is effective on repetitive data but expands non-repetitive strings.
