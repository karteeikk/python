def count_consonants(string):
    consonants ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count
# Input string from user
input_string = input("Enter a string: ")
# Call the function to count consonants
consonant_count = count_consonants(input_string)
print(f"Total consonants in the string: {consonant_count}")