file = open("tempconv.txt","w")
file.write("Fahrenheit  Celsius\n")
def celsius_convertor(fahrenheitTemp):
    Celsius = round(((fahrenheitTemp-2) * 5/9),2)
    return Celsius
for i in range(-10,11,1):
    file.write(str(i)+".00"+"\t\t\t"+str(celsius_convertor(i))+"\n")

    