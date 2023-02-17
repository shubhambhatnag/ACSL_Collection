import sys
output = []
file = open("expressions.txt","r")
for line in file.readlines():
    wrong = False
    line = line.rstrip()
    exp = line.split(" ")
    operators = ["+","-","/","*","^","%"]
    for i in range(len(exp)):            
        for op in operators:
            if op in exp[i] and len(exp[i]) > 1:
                if op == "+" or op == "-":
                    if len(exp[i]) > 2:
                        wrong = True
                else:
                    wrong = True
            if exp[i] == op and i == 0:
                wrong = True
        if list(exp[i])[0] == "0" and len(exp[i]) > 1:
            wrong = True
    if wrong == True:
        output.append("Invalid Expression")
        continue
    while len(exp) > 1:
        for item in range(len(exp)):
            if exp[item] in operators:
                if exp[item] == "+":exp[item] = int(exp[item-1]) + int(exp[item+1])
                elif exp[item] == "-":exp[item] = int(exp[item-1]) - int(exp[item+1])
                elif exp[item] == "/":exp[item] = int(exp[item-1]) / int(exp[item+1])
                elif exp[item] == "*":exp[item] = int(exp[item-1]) * int(exp[item+1])
                elif exp[item] == "^":exp[item] = int(exp[item-1]) ** int(exp[item+1])
                elif exp[item] == "%":exp[item] = int(exp[item-1]) % int(exp[item+1]) 
                exp.pop(item-1)
                exp.pop(item)
                break
    output.append(exp[0])
for i in output:print(i)
    
        
