def count_word_occurrences(text, word):
    words = text.lower().split()
    return words.count(word.lower())


text = input("Enter a sentence: ")
word = input("Enter the word to count: ")

result = count_word_occurrences(text, word)

print("Word occurrences:", result)
