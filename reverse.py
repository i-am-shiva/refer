s = input("Enter the string: ")

freq = {}

# Step 1: Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break