letterList = []
vowelList = ["a","e","i","o","u"]
enders = [" ",".","?","!",","]
words = ""
largestWord = [""]
vowelCount = 0
capitalCount = 0
letterDict = {}
sentence = list(input())
for char in sentence:
    if char.lower() in vowelList:
        vowelCount += 1
    if char not in enders:
        words += char.lower()
    else:
        if len(words) > len(largestWord[0]):
            largestWord = [words]
        elif len(words) == len(largestWord[0]):
            largestWord.append(words)
        words = ""
    if char == " " or char == "," or char == "?" or char == "." or char == "!":
        continue
    if char.lower() in letterDict:
        letterDict[char.lower()] += 1
    else:
        letterDict[char.lower()] = 1
    if char.upper() == char:
        capitalCount += 1
    if char.lower() in letterList:
        continue
    else:
        letterList.append(char.lower())
print(len(letterList))
print(vowelCount)
print(capitalCount)
print(max(letterDict.values()))
largestWord.sort()
print(largestWord[0])
