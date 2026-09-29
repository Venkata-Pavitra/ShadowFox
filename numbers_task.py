#Question 1
def format_number(number,character):
    return format(number,character)
print(format_number(145,'o')) 


#Question 2
radius=84
pi=3.14
area=pi*radius*radius
print("Area of the pond =",area)

radius=84
pi=3.14
water_per_square_meter=1.4
area=pi*radius*radius
water=area * water_per_square_meter
print("Total water in the pond =",int(water),"liters")


#Question 3
distance=490
time=7*60
speed=distance/time
print("Speed =",int(speed),"m/s")


