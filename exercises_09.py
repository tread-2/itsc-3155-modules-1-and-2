# Create a list to store words
words_list = []

# Take input for 5 words
for _ in range(5):
    word = input("Enter a word: ")
    words_list.append(word)

# Store each word from word_list into a single string with spacing
single_string = " ".join(words_list)

print("List of words:", words_list)
print("Single string: ", single_string)