import csv
import time

outputwords = []

def reverse_autocorrect(tempword="", position=0):
    if position == word_len:
        if tempword in same_length:
            outputwords.append(tempword)
        return 
    for letter in options[position]:
        if tempword+letter in prefix_set:
            reverse_autocorrect(tempword+letter,position+1)

input_word = input("Enter your word: ")
word_len = len(input_word)

with open("letters.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    letters = dict(reader)

options = []
for letter in input_word:
    options.append(letters[letter].split(","))

full_dict = open("words_alpha.txt","r")

same_length = set()
for word in full_dict:
    if len(word.strip()) == word_len:
        same_length.add(word.strip())

prefix_set = set()
for word in same_length:
    for prefix_len in range(1,word_len+1):
        prefix_set.add(word[:prefix_len])

start_time = time.perf_counter()
reverse_autocorrect()
end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time:.10f} seconds")

for word in outputwords:
    print(word)