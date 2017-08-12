for num in range(1, 10):
    prime = True
    for i in range(2, num):
        if (num%i== 0):
            break
        else:
            print(num)


