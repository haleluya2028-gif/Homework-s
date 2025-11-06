measurment = float (input (" enter your measurment "))
unit = input (" enter your desired unit(meter or feet)) ")
def unit_converter (measurment):
    if unit == "feet":
     print (str(measurment * 3.28)+ " feet ")
    elif unit == "meter":
     print (str(measurment / 3.28)+ " meter ")
    else :
            print (" try another value ")
unit_converter (measurment)
        
    