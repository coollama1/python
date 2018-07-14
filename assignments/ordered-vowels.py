def isVowel(s):
    if (s == "a") | (s == "e") | (s == "i") | (s == "o") | (s == "u"):
        return True
    return False

def numberOfVowels(s):
    count = 0
    for i in range(len(s)):
        pos = s[i]
        if isVowel(pos):
            count+=1
    return count

def vowelsInOrder(s):
    vowels = ["a", "e", "i", "o", "u"]
    pos = 0
    for i in range(len(s)):
        if pos <= 4:
            if(s[i] == vowels[pos]):
                pos+=1
    if pos == 5:
        return True

    return False

my_file = open("vowels-list.txt", "r")
wordList = my_file.readlines()

for i in range(len(wordList)):
    currentWord = wordList[i]
    if vowelsInOrder(currentWord) & (numberOfVowels(currentWord) == 5):
        print(currentWord)

my_file.close()
