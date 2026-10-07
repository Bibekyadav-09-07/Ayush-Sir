sentence = input("Enter a sentence: ")

# remove unnecessary spaces
sentence = "".join(sentence.split())

# convert to lowercase
sentence = sentence.lower()

# convert sentence into words
words = sentence.split()
#count total words
total_words = len(words)

# count python
python_count = words.count("python")

#Find the longest word

longest_word = max(words, key=len)

print("Clean sentence:", sentence)
print("Total number of words:", total_words)
print("Python appears:", python_count, "times")
print("Longest word:", longest_word)
