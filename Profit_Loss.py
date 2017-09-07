def quest():
    print("Enter NULL if value is not given/n")
    cp = float(input("Enter cost price: "))
    sp = float(input("ENter selling price: "))
    gp = ((sp - cp) / cp)* 100
    print("Profit% = ", gp)


def findcp():
    cp = float(input("Enter cost price: "))
    sp = float(input("Enter selling price: "))


quest()