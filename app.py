# Weight Converter Exercice
Weight = input("What is your weigth ? ")
Kilo_or_pounds = input("Type K for kg or L in pounds : ")

if Kilo_or_pounds.upper() == "K":
    Converted_weight = int(Weight) * 2.205
    print("Weight in Lbs is " + str(Converted_weight))
elif Kilo_or_pounds.upper() == "L":
    Converted_weight = int(Weight) / 2.205
    print("Weight in Kg is " + str(Converted_weight))
else:
    print("You must choose between (K)g and (L)bs !")