l = list()
new = list()

def new_list(ele):
    new.append(ele[0])
    new.append(ele[len(l)-1])
    print("New List:",(new))

def old_list():
    print("Press Enter twice when done\n")
    element = input("Enter Element: ")
    while(element):
        l.append(element)
        element = input("Enter Element: ")
    print("Original List: ", l)
    new_list(l)

old_list()

