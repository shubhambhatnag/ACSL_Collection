#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibCypher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER option
#  2. INTEGER num1
#  3. INTEGER num2
#  4. CHARACTER key
#  5. STRING msg
#

def fibCypher(option, num1, num2, key, msg):
    outputList = []
    if option == "E":   
        for letter in range(len(msg)):
            if(msg[letter]==''):
                continue
            if letter % 2 == 0:
                if letter == 0:
                    offset = ord(key) + num1
                else:
                    offset = ord(key) + (num1 + num2)
                    temp = num1
                    num1 = num2
                    num2 = temp + num2
            else:
                if letter == 1:
                    offset = ord(key) - num2
                else:
                    offset = ord(key) - (num1 + num2)
                    temp = num1
                    num1 = num2
                    num2 = temp + num2
            if letter == 18:
                print(offset)
            if offset > 122:
                offset = ((offset - 96) % 26) + 96 
            if offset < 97:
                offset = 96 - offset
                offset = 122 - (offset % 26)
    
            calculation = ord(msg[letter]) + 3 * offset
            outputList.append(str(calculation))
    
        return (" ".join(outputList))
    elif option == "D":  
        msg = msg.split(" ")
        for code in range(len(msg)):
            if(msg[code]==''):
                continue
            if code % 2 == 0:
                if code == 0:
                    offset = ord(key) + num1
                elif code == 1:
                    offset = ord(key) + num2
                else:
                    offset = ord(key) + (num1 + num2)
                    temp = num1
                    num1 = num2
                    num2 = temp + num2
    
            else:
                if code == 0:
                    offset = ord(key) - num1
                elif code == 1:
                    offset = ord(key) - num2
                else:
                    offset = ord(key) - (num1 + num2)
                    temp = num1
                    num1 = num2
                    num2 = temp + num2
            if offset > 122:
                offset = ((offset - 96) % 26) + 96
            if offset < 97:
                offset = 96 - offset
                offset = 122 - (offset % 26)
            calculation = int(msg[code])-(3*offset)
            outputList.append(chr(calculation))
        return ("".join(outputList))    
        
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    option = input()[0]

    num1 = int(input().strip())

    num2 = int(input().strip())

    key = input()[0]

    msg = input()

    result = fibCypher(option, num1, num2, key, msg)

    fptr.write(result + '\n')

    fptr.close()
