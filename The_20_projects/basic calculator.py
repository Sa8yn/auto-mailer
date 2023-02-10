#define the functions needed: add, sub, mul, div
def add(a,b):
    answer = a+b
    print(str(a)+" + "+str(b)+" = "+str(answer)+ "\n")

def sub(a,b):
    answer = a-b
    print(str(a)+" - "+ str(b)+" = "+str(answer)+ "\n")

def mult(a,b):
    answer = a*b
    print(str(a)+" x "+str(b)+" = "+str(answer)+ "\n")

def divi(a,b):
    answer = a/b
    print(str(a)+" / "+str(b)+" = "+str(answer)+ "\n")

while True:
    #print options to the user
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    #ask for values
    choice = input("Input your operation: ")
    #call the functions
    if choice == 'a' or choice == 'A':
        print("Addition")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        w = add(a,b)
    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        x = sub(a,b)
    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        y = mult(a,b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        z = divi(a,b)
    elif choice == 'e' or choice =='E':
        print("Exiting...")
        quit()
    else:
        print("Invalid operation" + "\n")

#while loop to continue the program until the user wants to exit
