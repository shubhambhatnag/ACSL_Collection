file = open("ACSL_JR_CONTEST_2.txt","r")
output = []
for line in file.readlines():
    line = line.rstrip()
    strings = line.split(" ")
    str1 = list(strings[0])
    str2 = list(strings[1])
    vowels = ["A","E","I","O","U"]
    delList = []
    for i in range(len(str1)-1):
        if str1[i] not in vowels and str1[i+1] not in vowels and str1[i] == str1[i+1]:
            delList.append(i+1)
    x = 0
    for i in delList:
        str1.pop(i-x)
        x+=1
    delList = []
    for i in range(len(str2)-1):
        if str2[i] not in vowels and str2[i+1] not in vowels and str2[i] == str2[i+1]:delList.append(i+1)
    x = 0
    for i in delList:
        str2.pop(i-x)
        x+=1
    while True:
        foundVowel = False
        for i in range(len(str1)):
            if str1[i] in vowels and i != 0:
                str1.pop(i)
                foundVowel = True
                break
        if foundVowel == False:break
    while True:
        foundVowel = False
        for i in range(len(str2)):
            if str2[i] in vowels and i != 0:
                str2.pop(i)
                foundVowel = True
                break
        if foundVowel == False:break
    while True:
        found = False
        for i in range(min(len(str1),len(str2))):
            if str1[i] == str2[i]:
                str1.pop(i)
                str2.pop(i)
                found = True
                break
        if found == False:break
    while True:
        found = False
        for i in range(min(len(str1),len(str2))):
            if str1[-1*(i+1)] == str2[-1*(i+1)]:
                str1.pop(-1*(i+1))
                str2.pop(-1*(i+1))
                found = True
                break
        if found == False:break
    if len(str1) < len(str2):output.append("".join(str1))
    elif len(str1) > len(str2):output.append("".join(str2))
    else:output.append(min("".join(str2),"".join(str1)))
for i in output:print(i)
    
        
        
