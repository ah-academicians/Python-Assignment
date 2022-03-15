def substitutionDecrypt(cipherText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = alphabet.find(ch)
        plainText = plainText + key[idx]
    return plainText

testKey1 = "zyxwvutsrqponmlkjihgfedcba "
plainText = substitutionDecrypt("gsv jfrxp yildm ulc",testKey1)
print(plainText)