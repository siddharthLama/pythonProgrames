inputString = input("enter a string")
charecterCount = 0
wordCount = 1
for i in inputString :
    charecterCount += 1
    if i == " " : 
        charecterCount = charecterCount - 1
        wordCount += 1
print(wordCount)
print(charecterCount)