import random
def three_heads():
    heads = 0
    while True:
        #1 represents head and 0 represents T
        toss = random.randint(0,1)
        if toss == 1:
            print("H",end = " ")
            heads+=1
            if heads == 3:
                print()
                break
        else:
            print(" T",end = " ")
            heads = 0
three_heads()            