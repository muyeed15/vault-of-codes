def t1(number):
    print("--------------t1---------------")
    for i in range(1, number+1):
        print(f"{i}"*i, end="\n")
    print("\n")


t1(5)

def t2(number):
    print("--------------t2---------------")
    for i in range(1, number+1):
        print(" "*(number - i) + f"{i}"*i, end="\n")
    print("\n")


t2(5)

def t3(number):
    print("--------------t3---------------")
    for i in range(1, number+1):
        print(" "*int((number - i)/2) + f"{i}"*i, end="\n")
    print("\n")


t3(5)


def t4(number):
    print("--------------t4---------------")
    for i in range(1, number+1):
        print(f"{i}"*(number - i + 1), end="\n")
    print("\n")


t4(5)

def t5(number):
    print("--------------t5---------------")
    for i in range(1, number+1):
        print(" "*(i-1) + f"{i}"*(number - i + 1), end="\n")
    print("\n")


t5(5)

def t6(number):
    print("--------------t6---------------")
    for i in range(1, number+1):
        print(" "*int((i-1)/2) + f"{i}"*(number - i + 1), end="\n")
    print("\n")


t6(5)

def t7(number):
    print("--------------t7---------------")
    for i in range(1, number+1):
        print(f"*"*(i) + " "*2*(number - (i)) + f"*"*(i), end="\n")
    print("\n")


t7(10)


def t8(number):
    print("--------------t8---------------")
    for i in range(1, number+1):
        print(f"*"*(number - i + 1) + " "*2*(i - 1) + f"*"*(number - i + 1), end="\n")
    print("\n")


t8(10)



def t9(number):
    print("--------------t9---------------")
    i = 1
    while i < 2*(number+1):

        if i > 2*(number) - 1:
            break

        if i > number:
            print(f"*"*(i - number + 1) + " "*2*(2*number - (i) - 1) + f"*"*(i - number + 1), end="\n")
        else:
            print(f"*"*(number - i + 1) + " "*2*(i-1) + f"*"*(number - i + 1), end="\n")

        i += 1
        
    print("\n")


t9(10)
