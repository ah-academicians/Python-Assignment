fileName = input("Enter fle name: ")
file = open(fileName,"r")
lines = file.readlines()
dictionary = {}
for line in lines:
    for i in line:
        if i.isalpha():
            if i.lower() not in dictionary.keys():
                dictionary[i.lower()] = line.lower().count(i.lower())
            else:
                dictionary[i.lower()] = dictionary[i.lower()]+line.lower().count(i.lower())
        else:
            continue
print("Letter   Count")
for i in sorted (dictionary.keys()) :
     print(i, "\t",dictionary[i],end = "\n")