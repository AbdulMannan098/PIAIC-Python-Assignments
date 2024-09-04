squares=[]
for i in range(2,10):
    print(i)
    
rangedList=list(range(2,10))
print(rangedList)

for rl in rangedList:
    rl=rl*2
    squares.append(rl)

print(squares)

squaredList=[rl*2 for rl in rangedList]
print(squaredList)

newList=["Banana","mangoes","apple","Peach","Grapes"]
newList.append("Dates")
print(newList)
newList.insert(0,"Almond")
print(newList)
guests=['Sajid',"Tahir","Asad","Hasan"]
print(f"Mr {guests[0]}!, I would like to invite you to dinner")
print(f"Mr {guests[1]}!, I would like to invite you to dinner")
print(f"Mr {guests[2]}!, I would like to invite you to dinner")
print(f"Mr {guests[3]}!, I would like to invite you to dinner")

guests=['Sajid',"Tahir","Asad","Hasan"]
for guest in guests:
    print(f"Mr {guest}!, I would like to invite you to dinner")

print(f"Unfortunately, {guests[1]} can't make it to dinner.")
guests.remove()

for guest in guests:
    print(guest)
