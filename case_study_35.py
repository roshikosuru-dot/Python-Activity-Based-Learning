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
