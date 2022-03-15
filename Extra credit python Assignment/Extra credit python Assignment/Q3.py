file = open("WorldSeries.txt","r")
lines = file.readlines()
yearWiseDictoinary = {}
teamWiseDictionary = {}
startingYear = 1903
for line in lines:
    if startingYear in [1904,1994]:
        startingYear += 1
        continue
    else:
        yearWiseDictoinary[startingYear] = line.strip()
        if line.strip() not in teamWiseDictionary.keys():
            teamWiseDictionary[line.strip()]=1
            startingYear += 1
        else:
            teamWiseDictionary[line.strip()] += 1
            startingYear += 1
while True:            
    year = int(input("Enter a year in the range 1903-2020: "))
    if year in range(1903,2021):
        if year in [1904,1994]:
            print("World series were not played this year.")
        else:
            print("The team that won the world series in ",year, " is ",yearWiseDictoinary[year], " They won the world series ",teamWiseDictionary[yearWiseDictoinary[year]],"times.")
    loop = input("Do you want to continue, type 'y' for yes and n for 'no': ")
    if loop.lower() == 'n':
        break