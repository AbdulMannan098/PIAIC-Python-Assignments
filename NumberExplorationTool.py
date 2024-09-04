name=input("Enter Your Name: ")
num1=int(input("Enter Your first Favorite Number: "))
num2=int(input("Enter Your Second Favorite Number: "))
num3=int(input("Enter Your Third Favorite Number: "))

print(f"\nHello, {name} Let's explore your favorite numbers:")
numList=[]
numList.append(num1)
numList.append(num2)
numList.append(num3)

# Creating a list to store tuples of the number and whether it is "even" or "odd"
evenOddList=[]
for num in numList:
    if num%2==0:
        evenOddList.append((num,"even"))
    else:
        evenOddList.append((num,"odd"))

for num, status in evenOddList:
    print(f"The Number {num} is {status}.")

for num in numList:
    squared_tuple = (num, num ** 2)
    print(f"The Number {num} and its square: {squared_tuple} ")


numbersSum=sum(numList)
print(f"\nAmazing! The sum of your three favorite numbers is {numbersSum}.")

#checking whether the sum of numbers is prime or not
if numbersSum>1:
    for num in range(2,numbersSum):
        if (numbersSum%num)==0:
            print(f"The sum of your three favorite numbers is not prime.")
            break
    else:
        print(f"The sum of your three favorite numbers is prime.")
else:
        print(f"The sum of your three favorite numbers is not prime.")


# Creating a list to store tuples of the number and whether it is "prime" or "not prime"
# primeList=[]
# for num in numList:
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 primeList.append((num,"not prime"))
#                 break
#         else:
#             primeList.append((num,"prime"))
#     else:
#         primeList.append((num,"not prime"))

# # Creating a list to store tuples of the number and whether it is "perfect" or "not perfect"    
# perfectList=[]
# for num in numList:
#     sum=0
#     for i in range(1,num):
#         if (num%i)==0:
#             sum+=i
#     if sum==num:
#         perfectList.append((num,"perfect"))
#     else:
#         perfectList.append((num,"not perfect"))

# print(f"Even or Odd: {evenOddList}")
# print(f"Prime or Not Prime: {primeList}")
# print(f"Perfect or Not Perfect: {perfectList}")