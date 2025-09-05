word = "APPLE"
frequent = max(set(word), key=word.count)

print("Most frequent character is:", frequent)
print("Frequency:", word.count(frequent))
