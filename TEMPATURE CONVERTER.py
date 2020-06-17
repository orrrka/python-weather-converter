temperature = str(input("Hello! \nInsert the temperature you would like to convert:"))

def conversion(temperature):
    if len(temperature)<2:
        return "Temperature is invalid, please add c or f."
    elif "C" in temperature:
        num=temperature.replace("C" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"F"
    elif "c" in temperature:
        num=temperature.replace("c" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"f"    
    elif "F" in temperature:
        num=temperature.replace("F" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"C"
    elif "f" in temperature:
        num=temperature.replace("f" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"c"
    else:
        return "Temperature is invalid, please try again."


print(conversion(temperature))

