# Count the number of unique characters in the input string.
# Print True if the number of unique characters is greater than 10,
# otherwise print False.

text = input()

unique_symbols = set(text)
unique_symbols_count = len(unique_symbols)

# Main solution
print(unique_symbols_count > 10)

# Alternative solution using if/else
# if unique_symbols_count > 10:
#     print(True)
# else:
#     print(False)