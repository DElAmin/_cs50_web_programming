from square import square
#import square
import sys


# a List
names = ["ElAmin"]

names.append("Abdou")
print(names)

names.sort()
print(names)

# a Set
s = set()
s.add(1)
print(s)

s.remove(1)
print(s)

#print(f"The set has {len(s)} elements")

#for i in [1, 2, 3]:
#    print(i)

#for i in range(6):
#    print(i)

for character in names[0]:
    print(character)

houses = {"Harry": "Gryfindor", "Draco": "Slytherin"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"
print(houses)

for i in range(6):
    print(square(i))    
    #print(square.square(i))

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione0", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print("Added " + person + "to flight successfully.")
    else:
        print("No available seats for " + person)

def annouce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@annouce
def hello():
    print("Hello, word!")

hello()

people = [
    {"name": "Harry", "house": "Gryfindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cho", "house": "Ravenclaw"}
]

def f(person):
    return person["house"]

people.sort(key=lambda person: person["name"])
print (people)

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x /y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print("Result of dicision is : " + result)