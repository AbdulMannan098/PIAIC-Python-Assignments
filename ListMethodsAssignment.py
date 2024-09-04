# Exercise 3-1
names = ["Abdullah", "Ali", "Abdul Hannan","Safi"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
for name in names:
    print(name)
    
# Exercise 3-2
names = ["Abdullah", "Ali", "Abdul Hannan","Safi"]
print(f"Hello, {names[0]}! How are you Today")
print(f"Hello, {names[1]}! How are you Today")
print(f"Hello, {names[2]}! How are you Today")
print(f"Hello, {names[3]}! How are you Today")

for name in names:
    print(f"Hello, {name}! How are you Today")

# Exercise 3-3
favorite_transport_modes=['Honda MotorCycle', "Tesla Car", "Yamaha Bike"]
print(f"I Would like to own a {favorite_transport_modes[0]}")
print(f"I Would like to own a {favorite_transport_modes[1]}")
print(f"I Would like to own a {favorite_transport_modes[2]}")
for mode in favorite_transport_modes:
    print(f"I Would like to own a {mode}")

# Exercise 3-4
guests=['Sajid',"Tahir","Asad","Hasan"]
print(f"Mr {guests[0]}!, I would like to invite you to dinner")
print(f"Mr {guests[1]}!, I would like to invite you to dinner")
print(f"Mr {guests[2]}!, I would like to invite you to dinner")
print(f"Mr {guests[3]}!, I would like to invite you to dinner")
for guest in guests:
    print(f"Mr {guest}!, I would like to invite you to dinner")


# Exercise 3-5
print(f"Unfortunately, {guests[0]} can't make it to dinner.")
guests.remove('Sajid')
guests.insert(0,"Ali")
print(f"Mr {guests[0]}!, I would like to invite you to dinner")
print(f"Mr {guests[1]}!, I would like to invite you to dinner")
print(f"Mr {guests[2]}!, I would like to invite you to dinner")
print(f"Mr {guests[3]}!, I would like to invite you to dinner")

# Exercise 3-6
guests=['Sajid',"Tahir","Asad","Hasan"]
print("Good news! We found a bigger table for dinner.")
guests.insert(0,"Hamid")
guests.insert(2,"Abdul Hannan")
guests.append("Abdul")

print(f"Mr {guests[0]}!, I would like to invite you to dinner")
print(f"Mr {guests[1]}!, I would like to invite you to dinner")
print(f"Mr {guests[2]}!, I would like to invite you to dinner")
print(f"Mr {guests[3]}!, I would like to invite you to dinner")
print(f"Mr {guests[4]}!, I would like to invite you to dinner")
print(f"Mr {guests[5]}!, I would like to invite you to dinner")
print(f"Mr {guests[6]}!, I would like to invite you to dinner")

# Exercise 3-7
print("Unfortunately, the table won't arrive in time for dinner, I can only invite two people for dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")

print(f"{guests[0]}, you are still invited to dinner.")
print(f"{guests[1]}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)

# Exercise 3-8
places = ['Japan', 'Norway', 'New Zealand', 'Iceland', 'Canada']
# Original order
print("Original list:", places)

# Alphabetical order
print("Alphabetical order:", sorted(places))

# Original list again
print("Original list:", places)

# Reverse alphabetical order
print("Reverse alphabetical order:", sorted(places, reverse=True))

# Original list again
print("Original list:", places)

# Reverse the list order
places.reverse()
print("Reversed list:", places)

# Reverse back to original
places.reverse()
print("Back to original order:", places)

# Sort alphabetically
places.sort()
print("Sorted alphabetically:", places)
# Sort in reverse alphabetical order
places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)

# Exercise 3-9
languages = ['Python', 'JavaScript', 'C++', 'Java', 'Ruby']
# Using append
languages.append('Go')
print("After append:", languages)
# Using insert
languages.insert(2, 'C#')
print("After insert:", languages)
# Using remove
languages.remove('Ruby')
print("After remove:", languages)
# Using pop
popped_language = languages.pop()
print("After pop:", languages)
print("Popped language:", popped_language)
# Using sort
languages.sort()
print("After sort:", languages)
# Using reverse
languages.reverse()
print("After reverse:", languages)
# Using count (though not necessary here)
count_of_java = languages.count('Java')
print("Count of 'Java':", count_of_java)
# Using index
index_of_python = languages.index('Python')
print("Index of 'Python':", index_of_python)
# Using clear
languages.clear()
print("After clear:", languages)


















# print(f"Unfortunately, {guests[1]} can't make it to dinner.")
# guests.remove()

# for guest in guests:
#     print(guest)