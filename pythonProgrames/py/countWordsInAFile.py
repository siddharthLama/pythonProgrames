def countWordsInAFile() :
    fileName = input("enter the file name")
    numberOfWords = 0
    file = open(fileName,"r")
    for line in file :
        words = line.split()
        print(line)
        print(words)
        print(len(words))
        numberOfWords = numberOfWords +len(words)
    print (numberOfWords)
countWordsInAFile()