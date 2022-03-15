outPutFile = open("best_and_worst.txt","w")
file = open("riskfactors.csv")
lines = file.readlines()
heartDiseaseDeathRate = {}
motorVehicleDeathRate = {}
teenBirth = {}
adultSmoking = {}
adultObesity = {}
lineNumber = 0
for line in lines:
    if lineNumber < 6:
        lineNumber+=1
    else:
        try:
            heartDiseaseDeathRate[line.split(",")[0]]=float(line.split(",")[1].strip("%"))
            motorVehicleDeathRate[line.split(",")[0]]=float(line.split(",")[5].strip("%"))
            teenBirth[line.split(",")[0]]=float(line.split(",")[7].strip("%"))
            adultSmoking[line.split(",")[0]]=float(line.split(",")[11].strip("%"))
            adultObesity[line.split(",")[0]]=float(line.split(",")[13].strip("%"))
        except:
            continue
def largest(dictionary):
    values = dictionary.values()
    maxValue = max(values)
    maxKey = ""
    for i in dictionary.keys():
        if dictionary[i]==maxValue:
            maxKey = i
    return [maxValue,maxKey]
def smallest(dictionary):
    values = dictionary.values()
    minValue = min(values)
    minKey = ""
    for i in dictionary.keys():
        if dictionary[i]==minValue:
            minKey = i
    return [minValue,minKey]
#print(largest(heartDiseaseDeathRate))
#print(smallest(heartDiseaseDeathRate))
outPutFile.write("Output of the file best_and_worst.txt: \n")
outPutFile.write("indicator\t\t Max \t\t Min\n")
outPutFile.write("------------------------------------------\n")
outPutFile.write("------------------------------------------\n")
outPutFile.write("heart Disease Death Rate (2007):\n")
outPutFile.write(str(largest(heartDiseaseDeathRate)[1])+"\t\t"+str(largest(heartDiseaseDeathRate)[0])+"\n")
outPutFile.write(str(smallest(heartDiseaseDeathRate)[1])+"\t\t\t\t"+str(smallest(heartDiseaseDeathRate)[0])+"\n")
outPutFile.write("Motor Vehicle Death Rate(2009): \n")
outPutFile.write(str(largest(motorVehicleDeathRate)[1])+"\t\t"+str(largest(motorVehicleDeathRate)[0])+"\n")
outPutFile.write(str(smallest(motorVehicleDeathRate)[1])+"\t\t\t\t"+str(smallest(motorVehicleDeathRate)[0])+"\n")
outPutFile.write("Teen Birth Rate (2009): \n")
outPutFile.write(str(largest(teenBirth)[1])+"\t\t"+str(largest(teenBirth)[0])+"\n")
outPutFile.write(str(smallest(teenBirth)[1])+"\t\t\t\t"+str(smallest(teenBirth)[0])+"\n")
outPutFile.write("Adult Smoking :\n")
outPutFile.write(str(largest(adultSmoking)[1])+"\t\t"+str(largest(adultSmoking)[0])+"\n")
outPutFile.write(str(smallest(adultSmoking)[1])+"\t\t\t\t"+str(smallest(adultSmoking)[0])+"\n")
outPutFile.write("Adult Obesity (2010): \n")
outPutFile.write(str(largest(adultObesity)[1])+"\t\t"+str(largest(adultObesity)[0])+"\n")
outPutFile.write(str(smallest(adultObesity)[1])+"\t\t\t\t"+str(smallest(adultObesity)[0])+"\n")