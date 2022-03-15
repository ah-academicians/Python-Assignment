file = open("books.txt","r")
lines = file.readlines()
booksDictionary = {}
for line in lines:
    AuthorAndBooks = line.strip().split(",")
    booksDictionary[AuthorAndBooks[1].strip()] = AuthorAndBooks[0].strip()
for i in sorted (booksDictionary.keys()) :
     print(i,"[",booksDictionary[i],"]", end = "\n")