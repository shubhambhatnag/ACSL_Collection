inputFile = open(input("File name: "),"r")
outputList = []



for line in inputFile.readlines():
    output = []
    line = line.split(" ")
    num = line[0]
    length = int(line[1])
    if int(num) < 1 or int(length < 1):
        print("Postive numbers only.")
        continue
    num = list(num)
    while True:
        temp = ""
        for i in range(0,length):
            temp += (num[i])
        output.append(int(temp))
        if len(num) < length:
            outputList.append(sum(output))
            break
        else:
            num.pop(0)

print(outputList)        
