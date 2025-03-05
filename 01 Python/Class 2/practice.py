#Comparison Operators
print(45 != 54) 
print(True and False) #and
print(True or False) #or

#List adding and changing elements
countries = [
    "Pakistan",
    "China",
    "Afghanistan"
]

print(type(countries))

print(countries[0])
print(countries[2])
print(countries[1])

countries.append("India")

print(countries)

countries.insert(0, "South Korea")

print(countries)

countries[2] = "Italy"

print(countries)

#Lists: Taking Slice out of them

print(countries[1:4])

print(countries[:3])

print(countries[2:])

#print using negative index

print(countries[-4:-1])

print(countries[-5:-2])

print(countries[-3:])

#Lists: Deleting & Removing Elements

del countries[0]

print(countries)

countries.remove("India")

print(countries)

#Lists: popping element

country = countries.pop(1)

print(country)

print(countries)

#Conditional Statements

is_ramadan = True

if is_ramadan:
    print("Timing: 10:00 to 1:00 PM")
else:
    print("Timing: 06:00 to 9:00 PM")