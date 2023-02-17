s = "Roses are red. Violets are blue. I love you. And so do you."

def findLastOctal(s):
    # Write your code here
    s = list(s)
    for i in range(len(s)):
        s[i] = ord(s[i])
    #print(s)
    for i in range(len(s)):
        binary = bin(int(s[i]))[2:]
        while len(binary) < 8:
            binary = "0" + binary
        s[i] = binary
    #print(s)  
    s = "".join(s)
    #print(s)
    count = 0
    
    while True:
        num = bin(count)[2:]
        curr = len(s)
        s = s.replace(num,"",1)
        found = False
        if (curr != len(s)):
            found = True
        s = s[::-1]
        curr = len(s)
        s = s.replace(num[::-1],"",1)
        if (curr != len(s)):
            found = True
        s = s[::-1]
        if (found == False):
            break
        count += 1
    

    num = int(s, 2)
    num = oct(num)
    s = num[2:]
    
    count = 0
    
    while True:
        num = oct(count)[2:]
        curr = len(s)
        s = s.replace(num,"",1)
        found = False
        if (curr != len(s)):
            found = True
        s = s[::-1]
        curr = len(s)
        s = s.replace(num[::-1],"",1)
        if (curr != len(s)):
            found = True
        s = s[::-1]
        if (found == False):
            break
        count += 1
    return(count - 1)

print(findLastOctal(s))