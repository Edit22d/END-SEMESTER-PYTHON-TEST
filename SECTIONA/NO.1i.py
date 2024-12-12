#calculate area of a circle
def area_circle():
    radius = int(input('Enter the radius of the circle in parameter:\t'))
    import math
    pie = math.pi
    area =math.pi*radius**2
    return(f'The area of the circle with {pie} and raius of {radius**2} is {area}')
area_circle()