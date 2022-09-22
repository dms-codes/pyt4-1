word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input()
user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter in ("A","I","E","U","O"):
        continue
    word_without_vowels+=letter


# Print the word assigned to word_without_vowels.
print(word_without_vowels)
