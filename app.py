# Weight Converter Exercice

# Getting answer for these questions inside variables 
Weight = input("What is your weigth ? ")
Kilo_or_pounds = input("Type K for kg or L in pounds : ")

# transforming user's answer to uppercase with upper()
if Kilo_or_pounds.upper() == "K":
    # converting to integer the answer (that is of type "string")
    Converted_weight = int(Weight) * 2.205
    # converting the result of the converted weight into type of string to be able to concatenate and printing it
    print("Weight in Lbs is " + str(Converted_weight))
elif Kilo_or_pounds.upper() == "L":
    Converted_weight = int(Weight) / 2.205
    print("Weight in Kg is " + str(Converted_weight))
# if user enters something else than "K" or "L"
else:
    print("You must choose between (K)g and (L)bs !")