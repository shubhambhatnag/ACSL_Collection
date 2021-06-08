#Created by Shubham Bhatnagar
output = []
file = open("ACSL_JR_CONTEST_1.txt","r")
for line in file.readlines():
    try:
        nums = (line.rstrip()).split(" ")
        n = list(nums[0])
        p = nums[1]
        d = nums[2]
        if int(n[len(n)-int(p)]) >= 0 and int(n[len(n)-int(p)]) <= 4:
            n[len(n)-int(p)] = str((int(n[len(n)-int(p)])+int(d))%10)
            n = n[:(len(n)-int(p)+1)]
            for i in range(len(list(nums[0]))-len(n)):
                n.append("0")
        else:
            n[len(n)-int(p)] = list(str(abs(int(n[len(n)-int(p)])-int(d))))[0]
            n = n[:(len(n)-int(p)+1)]
            for i in range(len(list(nums[0]))-len(n)):
                n.append("0")
        output.append("".join(n))
    except:
        output.append("error")
for i in output:
    print(i)
        
        
