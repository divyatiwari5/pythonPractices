p = input("Enter password:")

# if any(i.isdigit() for i in p):
#    print(p)

if any(t.isdigit() for t in p) and any(t.isalpha() for t in p):
    print(p)
else:
    print("Enter valid password")
