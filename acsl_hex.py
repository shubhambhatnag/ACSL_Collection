inputHex = input().split(" ")
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
hexPosition = list(inputHex[0])
hexPosition[1] = int(hexPosition[1])
turns = list(inputHex[1])
for turn in turns:
    mode = None
    if alpha.index(hexPosition[0])%2 == 0:
        mode = "even"
    else:
        mode = "odd"
    if turn == "1":
        hexPosition[1] += 1
    elif turn == "2":
        if mode == "even":
            hexPosition[0] = alpha[alpha.index(hexPosition[0])+1]
            hexPosition[1] += 1
        else:
            hexPosition[0] = alpha[alpha.index(hexPosition[0])+1]
    elif turn == "3":
        if mode == "even":
            hexPosition[0] = alpha[alpha.index(hexPosition[0])+1]
        else:
            hexPosition[0] = alpha[alpha.index(hexPosition[0])+1]
            hexPosition[1] -= 1
            
    elif turn == "4":
        hexPosition[1] -= 1
    elif turn == "5":
        if mode == "even":
            hexPosition[0] = alpha[alpha.index(hexPosition[0])-1]
        else:
            hexPosition[0] = alpha[alpha.index(hexPosition[0])-1]
            hexPosition[1] -= 1
    elif turn == "6":
        if mode == "even":
            hexPosition[0] = alpha[alpha.index(hexPosition[0])-1]
            hexPosition[1] += 1
        else:
            hexPosition[0] = alpha[alpha.index(hexPosition[0])-1]
hexPosition[1] = str(hexPosition[1])
print("".join(hexPosition))
