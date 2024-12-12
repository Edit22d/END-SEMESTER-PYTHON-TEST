# calculating a car's
def car_miles():
    miles_driven =float(input('Enter the miles driven:\t'))
    gallons_used = float(input('Enter gallons of gas used:\t'))
    MPG = miles_driven / gallons_used
    print(f'A car drives {miles_driven} miles per gallon of {gallons_used} is {MPG}')
car_miles()

    