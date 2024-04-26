word = input("Enter a word: ")
# Convert the word into a list of characters
char_list = list(word)
# Remove vowels from the list
vowels = ['a', 'e', 'i', 'o', 'u']
char_list = [i for i in char_list if i.lower() not in vowels]
print("Old List:", list(word))
print("New List:", char_list)
