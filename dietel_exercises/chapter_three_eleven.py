stopper = 0;

while stopper != -1:
    miles_driven = float(input("Enter the miles driven: " "Enter -1 to stop"))
    gallons_used= float(input("Enter the gallons used: "))

    miles_per_gallon = miles_driven / gallons_used
    print("The miles per gallon used is: ", miles_per_gallon)

    addition  = miles_per_gallon + gallons_used
    print("their sum is: ",addition)

    average = addition / 2.0
    print("their average is :", average)

