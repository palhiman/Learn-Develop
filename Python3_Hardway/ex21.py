# Exercise 21: Functions can return something.

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just fuctions!!")

x = int(input("Enter first integer value >> "))
y = int(input("Enter second integer value >> "))

age = add(x, y)
height = subtract(x, y)
weight = multiply(x,y)
iq = divide(x,y)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

# A puzzle
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Try doing it by hand...")
