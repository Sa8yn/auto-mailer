def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
    answer = a-b
    print(str(a)+ "-" + str(b) + "="+ str(answer))

def mult(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def mod(a,b):
    answer = a % b
    print(str(a) + "%" + str(b) + "=" + str(answer))

while True:

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Modulo")
    print("F. Exit")

    choice = input("Choose an operation:")

    if choice == 'a' or choice == 'A':
        print("Addition")
        a = int(input("Enter for a:"))
        b = int(input("Enter for b:"))
        add(a,b)

    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        a = int(input("Enter for a:"))
        b = int(input("Enter for b:"))
        sub(a,b)

    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        a = int(input("Enter for a:"))
        b = int(input("Enter for b:"))
        mult(a,b)

    elif choice == 'd' or choice == 'D':
        print("division")
        a = int(input("Enter for a:"))
        b = int(input("Enter for b:"))
        div(a,b)

    elif choice == 'e' or choice == 'E':
        print("Modulo")
        a = int(input("Enter for a:"))
        b = int(input("Enter for b:"))
        mod(a,b)

    elif choice == 'f' or choice == 'F':
        print("Program Exited")
        quit()

    else:
        print("invalid operation")