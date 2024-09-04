#1 
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))
sum= num1+num2
print("The Sum of two your entered Numbers is:" + sum)
#2
fav_animal=input("Enter Your Favorite Animal:")
print(f"My Favorite Animal is Also {fav_animal}")
#3 
fahrenheitTemp=float(input("Enter Temperature in Fahrenheit: "))
calceusTemp=(fahrenheitTemp-32) *5.0/9.0
print("Your Entered Temperature in Fahrenheit is: " + calceusTemp)

#4 
side1=float(input("Enter length of 1st side of the triangle: "))
side2=float(input("Enter length of 2nd side of the triangle: "))
side3=float(input("Enter length of 3rd side of the triangle: "))
trianglePrimeters=side1+side2+side3
print("The Primeters of triangle is:" +trianglePrimeters)
#5
numberForSquare=float(input("Enter the number you want to know square:"))
squareOfNumber=numberForSquare * numberForSquare

#6
numlist=[1,2,3,4,5]
numlist=numlist.remove(3)
print(numlist)

#7 
list1=[1,2,3]
list2=[4,5,6]
list2=list2.extend(list1)
print(list2)
# for e in list1:
# list2.extend

#11 
contList=[]
for c in contList:
    number=input