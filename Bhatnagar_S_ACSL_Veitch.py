output = []
for inps in range(5):
    hexa = list(input())
    hexa[0] = str(bin(int(hexa[0], 16)))[2:]
    hexa[1] = str(bin(int(hexa[1], 16)))[2:]
    while len(hexa[0]) < 4:
        hexa[0] = "0"+hexa[0]
    while len(hexa[1]) < 4:
        hexa[1] = "0"+hexa[1]
    hexa[0] = list(hexa[0])
    hexa[1] = list(hexa[1])
    for i in range(len(hexa[0])):
        hexa[0][i] = int(hexa[0][i])
        hexa[1][i] = int(hexa[1][i])
    expression = []

    if hexa[0] == [1,1,1,1]:
        expression.append("B")
        hexa[0] = [0,0,0,0]
    if hexa[1] == [1,1,1,1]:
        expression.append("~B")
        hexa[1] = [0,0,0,0]
    if hexa[0][0] == 1 and hexa[0][1] == 1 and hexa[1][0] == 1 and hexa[1][1] == 1:
        expression.append("A")
        hexa[0][0] = 0
        hexa[0][1] = 0
        hexa[1][0] = 0
        hexa[1][1] = 0
    if hexa[0][1] == 1 and hexa[0][2] == 1 and hexa[1][1] == 1 and hexa[1][2] == 1:
        expression.append("C")
        hexa[0][1] = 0
        hexa[0][2] = 0
        hexa[1][1] = 0
        hexa[1][2] = 0
    if hexa[0][2] == 1 and hexa[0][3] == 1 and hexa[1][2] == 1 and hexa[1][3] == 1:
        expression.append("~A")
        hexa[0][2] = 0
        hexa[0][3] = 0
        hexa[1][2] = 0
        hexa[1][3] = 0
    if hexa[0][0] == 1 and hexa[0][3] == 1 and hexa[1][0] == 1 and hexa[1][3] == 1:
        expression.append("~C")
        hexa[0][0] = 0
        hexa[0][3] = 0
        hexa[1][0] = 0
        hexa[1][3] = 0
    if hexa[0][0] == 1 and hexa[0][1] == 1:
        expression.append("AB")
        hexa[0][0] = 0
        hexa[0][1] = 0
    if hexa[0][1] == 1 and hexa[0][2] == 1:
        expression.append("BC")
        hexa[0][1] = 0
        hexa[0][2] = 0
    if hexa[0][2] == 1 and hexa[0][3] == 1:
        expression.append("~AB")
        hexa[0][2] = 0
        hexa[0][3] = 0
    if hexa[1][0] == 1 and hexa[1][1] == 1:
        expression.append("A~B")
        hexa[1][0] = 0
        hexa[1][1] = 0
    if hexa[1][1] == 1 and hexa[1][2] == 1:
        expression.append("~BC")
        hexa[1][1] = 0
        hexa[1][2] = 0
    if hexa[1][2] == 1 and hexa[1][3] == 1:
        expression.append("~A~B")
        hexa[1][2] = 0
        hexa[1][3] = 0
    if hexa[0][0] == 1 and hexa[1][0] == 1:
        expression.append("A~C")
        hexa[0][0] = 0
        hexa[1][0] = 0
    if hexa[0][1] == 1 and hexa[1][1] == 1:
        expression.append("AC")
        hexa[0][1] = 0
        hexa[1][1] = 0
    if hexa[0][2] == 1 and hexa[1][2] == 1:
        expression.append("~AC")
        hexa[0][2] = 0
        hexa[1][2] = 0
    if hexa[0][3] == 1 and hexa[1][3] == 1:
        expression.append("~A~C")
        hexa[0][3] = 0
        hexa[1][3] = 0
    if hexa[0][0] == 1 and hexa[0][3] == 1:
        expression.append("B~C")
        hexa[0][0] = 0
        hexa[0][3] = 0
    if hexa[1][0] == 1 and hexa[1][3] == 1:
        expression.append("~B~C")
        hexa[1][0] = 0
        hexa[1][3] = 0
    if hexa[0][0] == 1:
        expression.append("AB~C")
    if hexa[0][1] == 1:
        expression.append("ABC")
    if hexa[0][2] == 1:
        expression.append("~ABC")
    if hexa[0][3] == 1:
        expression.append("~AB~C")
    if hexa[1][0] == 1:
        expression.append("A~B~C")
    if hexa[1][1] == 1:
        expression.append("A~BC")
    if hexa[1][2] == 1:
        expression.append("~A~BC")
    if hexa[1][3] == 1:
        expression.append("~A~B~C")


    output.append("+".join(expression))
for i in output:
    print(i)
