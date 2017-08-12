n = int(input("Enter number:"))
fact = n
for i in range(n-1, 0, -1):
    fact = fact*i
    print(i)
print("Factorial of ", n, "is:")
print(fact)
