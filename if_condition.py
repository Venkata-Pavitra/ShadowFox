#Question 1
height=float(input("Enter the height in meters:"))
weight=float(input("Enter the weight in kilograms:"))
bmi=weight/(height*height)
print("BMI",bmi)
if(bmi>=30):
    print("Obesity")
elif(bmi>=25):
    print("Overweight")
elif(bmi>=18.5):
    print("Normal")
else:
    print("Underweight")   


#Question 2
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=input("Enter a city:")
if(city in Australia):
    print(city, "is in Australia")
elif(city in UAE):
    print(city, "is in UAE")
elif(city in India):
    print(city, "is in India")
else:
    print("City not found")                 


#Question 3
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city1=input("Enter the first city:")
city2=input("Enter the second city:")
if(city1 in Australia and city2 in Australia):
    print("Both cities are in Australia")
elif(city1 in UAE and city2 in UAE):
    print("Both cities are in UAE")
elif(city1 in India and city2 in India):
    print("Both cities are in India")
else:
    print("They don't belong to the same country")        

