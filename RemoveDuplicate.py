string = str(input("Enter string: "))

slist = string.split()
done = []
for x in slist:
    if x not in done:
        print("Number of " + str(x) + ": " + str(slist.count(x)))
        done.append(x)

print(string)
print("Total no. of words:", len(string.split()))
print("Without duplicate:", ' '.join(done))