inputList = []
for i in range(5):
    inputList.append(input())
print(len(list(inputList[0])))
print(sum([int(d) for d in str(inputList[1])]))
temp = 0
for i in range(len(list(inputList[2]))):
    if i%2 == 0:
        temp += int(list(inputList[2])[i])
print(temp)
temp = 0
for i in inputList[3]:
    if i == "4":
        temp += 1
print(temp)
if len(list(inputList[4]))%2 == 0:
    print(list(inputList[4])[int(((len(list(inputList[4])))/2)-1)])
else:
    print(list(inputList[4])[int((len(list(inputList[4])))//2)])

