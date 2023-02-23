"""
    Author: Michael Fessler
    Date: 2023/02/22
    Version: 0.1
    Description:
            App to read a number of words from user input, store them in a list,
            then print the list to console and give a table of the amount of words
            in the list, how many duplicate entries etc.
"""

wordsList = []

nextInput = str(input("Enter word for the list (or 'CB23' to end input cycle): "))
if nextInput != "CB23":
    wordsList.append(nextInput)
while nextInput != "CB23":
    nextInput = str(input("Enter word for the list (or 'CB23' to end input cycle): "))
    if nextInput != "CB23":
        wordsList.append(nextInput)

wordsList.sort()

wordsSet = (set(wordsList))


for word in wordsList:
    print(word)

print("\nStats: ")

counter = 0
for word in wordsSet:
    for wordCheck in wordsList:
        if word == wordCheck:
            counter += 1
    print(word + " " + str(counter))
    counter = 0