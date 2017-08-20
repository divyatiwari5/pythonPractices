name = input("Enter your name: ")
age = int(input("Enter your age: "))

def printdata():
    print("Your name is:", name)
    print("Your age is:", age)
    print("You'll turn 100 in ", 100-age ," years")

printdata()

n = int(input("Enter number: "))
for i in range (n):
    printdata()