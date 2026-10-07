sentence = input("Enter a sentence: ")

# convert to lowercase
sentence = sentence.lower()
# convert sentence into words
words = sentence.split()
#create empty dictionary
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
# Display results
for word, count in frequency.items():
    print(word,":", count)