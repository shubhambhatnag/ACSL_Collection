#Created by Shubham Bhatnagar
#ACSL Intermediate for Poolesville Highschool
output = []
file = open("ACSL_INT_CONTEST_1.txt","r")
for line in file.readlines():
    try:
        numInput = (line.rstrip()).split(" ")
        n,p = list(numInput[0]),numInput[1]
        for i in range(len(n)):
            if i < len(n)-int(p):n[i] = str((int(n[i])+int(n[len(n)-int(p)]))%10)
            elif i > len(n)-int(p):n[i] = str((abs(int(n[i])-int(n[len(n)-int(p)])))%10)
        n[int(p)-1] = str(n[int(p)-1])
        output.append("".join(n))
    except:output.append("error")
for i in output:print(i)
