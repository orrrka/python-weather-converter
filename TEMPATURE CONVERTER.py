temp = str(input("Hello! \nInsert the temperature you would like to convert:"))

def conversion(temp):
    if len(temp)<2:
        return "Temperature is invalid, please add c or f."
    elif "C" in temp:
        num=temp.replace("C" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"F"
    elif "c" in temp:
        num=temp.replace("c" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"f"    
    elif "F" in temp:
        num=temp.replace("F" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"C"
    elif "f" in temp:
        num=temp.replace("f" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"c"
    else:
        return "Temperature is invalid, please try again."


print(conversion(temp))



print(conversion(temperature))

