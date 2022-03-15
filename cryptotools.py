
def encrypt(text,k):
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            encrypted+=char
        elif (char.isupper()):
            encrypted += chr((ord(char) + k-65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + k - 97) % 26 + 97)
    return encrypted

def decrypt(text,k):
    plaintext = ''
    for i in text:
        if (i == ' '):
            plaintext += ' '
        elif (i.islower()):
            plaintext += chr((ord(i) - k - 97)% 26  + 97)
        else:
            plaintext += chr((ord(i) - k - 65)% 26  + 65)
    return plaintext

while True:
    option = input("press e to encypt or d to decrypt: ")
    if option.lower()=="e":
        text = input("enter plain text: ")
        key = int(input("enter key: "))
        print("encrypted message is :",encrypt(text, key))
    elif option.lower()=="d":
        text = input("enter cipher text: ")
        key = int(input("enter key: "))
        print("decrypted message is :",decrypt(text, key))
    else:
        print("you entered invalid arguments.")