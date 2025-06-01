s = " Here is i and u and the - demo is that how loop iterate in string"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print(f"Found {s[index]} at index {index}")

# Using a for loop to iterate through the string
for char in s:
    if char == 'i' or char == 'u':
        print(f"Found {char} in the string")
# Using a while loop to iterate through the string
index = 0
while index < len(s):
    if s[index] == 'i' or s[index] == 'u':
        print(f"Found {s[index]} at index {index}")
    index += 1
# Using a for loop with enumerate to get index and character
for index, char in enumerate(s):
    if char == 'i' or char == 'u':
        print(f"Found {char} at index {index}")
# Using a list comprehension to find all occurrences
found_chars = [char for char in s if char in 'iu']
print(f"Found characters: {found_chars}")
# Using a filter to find all occurrences
found_chars_filter = list(filter(lambda char: char in 'iu', s))
print(f"Found characters using filter: {found_chars_filter}")
# Using a generator expression to find all occurrences
found_chars_gen = (char for char in s if char in 'iu')
for char in found_chars_gen:
    print(f"Found character using generator: {char}")               