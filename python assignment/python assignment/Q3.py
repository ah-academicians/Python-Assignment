file = open("thisFile.txt","r")
file2 = open("thatFile.txt","w")
lines = file.readlines()
lineIndicator = 0
for line in lines:
    if lineIndicator%2==0:
        file2.write(line)
        lineIndicator+=1
    else:
        lineIndicator+=1