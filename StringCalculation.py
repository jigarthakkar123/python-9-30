s1=input("Enter A String : " )

u=l=c=s=n=0

for i in s1:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    if i.isalpha():
        c=c+1
    elif i.isnumeric():
        n=n+1
    elif i.isspace():
        s=s+1

print("Total Upper Case : ",u)
print("Total Lower Case : ",l)
print("Total Alphabets : ",c)
print("Total Numeric : ",n)
print("Total Space : ",s)
