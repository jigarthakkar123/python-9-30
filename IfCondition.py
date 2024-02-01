'''
1. Simple If

    if condition:
        statement

2. If/Else

    if condition:
        statement
    else:
        statement

3. Nested If

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

4. Ladder if

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
    
'''

a=float(input("Enter A : "))
b=float(input("Enter B : "))
c=float(input("Enter C : "))

if a>b:
    if a>c:
        print(a," Is Max")
    else:
        print(c," Is Max")
elif b>c:
    print(b," Is Max")
else:
    print(c," Is Max")
    
        
