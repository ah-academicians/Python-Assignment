def threeRailFenceCipher(plainText):
    rail1 = []
    rail2 = []
    rail3 = []
    position = 0
    for i in plainText:
        if position==0:
            rail1.append(i)
            position+=1
        elif position == 1:
            rail2.append(i)
            position+=1
        elif position == 2:
            rail3.append(i)
            position = 0
    output  = rail3 + rail2 + rail1
    return "".join(output)
print(threeRailFenceCipher("ABCDEFGHI"))