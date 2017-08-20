num1 = int(input("Enter Dividend: "))
num2 = int(input("Enter Divisor: "))

rem = num1%num2

if(rem%2 is 0):
    print("Remainder is even: ", rem)
else:
    print("Remainder is odd: ", rem)