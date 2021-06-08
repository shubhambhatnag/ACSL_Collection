outputList = []
for i in range(5):
    output = []
    inputData = input()
    inputData = inputData.split(" ")
    num = list(inputData[0])
    count = int(inputData[1])
    temp = ""
    for k in range(len(num)):
        temp = ""
        if len(num)- k == count-1:  
            break
        else:
            for g in range(count):
                temp += num[k+g] 
            output.append(int(temp))
    outputList.append(sum(output))
for i in range(outputList):
    print(i)
                    
    
