tempature = str(input("Hello! \nInsert the temperature you would like to convert:"))

def conversion(tempature):
    if len(tempature)<2:
        return "Tempature is invalid, please add c or f."
    elif "C" in tempature:
        num=tempature.replace("C" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"F"
    elif "c" in tempature:
        num=tempature.replace("c" , "")
        number = float(num)
        conversion = str((number*9+160)/5)
        return conversion+"f"    
    elif "F" in tempature:
        num=tempature.replace("F" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"C"
    elif "f" in tempature:
        num=tempature.replace("f" , "")
        number = float(num)
        conversion = str((number*5-160)/9)
        return conversion+"c"
    else:
        return "Tempature is invalid, please try again."


print(conversion(tempature))

