import UDF

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice : "))
    print("*"*40)
    if choice==1:
        n1=int(input("Enter Value : "))
        UDF.oddeven(n1)
        print("*"*40)
    elif choice==2:
        n1=int(input("Enter Value : "))
        n2=int(input("Enter Value : "))
        UDF.maxoftwo(n1,n2)
        print("*"*40)
    elif choice==3:
        n1=int(input("Enter Value : "))
        n2=int(input("Enter Value : "))
        n3=int(input("Enter Value : "))
        UDF.maxofthree(n1,n2,n3)
        print("*"*40)
    elif choice==4:
        n1=int(input("Enter Value : "))
        UDF.fibonacci(n1)
        print("*"*40)
    elif choice==5:
        n1=int(input("Enter Value : "))
        UDF.prime(n1)
        print("*"*40)
    elif choice==6:
        print("Thank You For Using Our Services")
        print("*"*40)
        break
    else:
        print("Invalid Choice. Please Try Again")
        print("*"*40)
            
        
