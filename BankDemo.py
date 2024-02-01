class Bank:

    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Insufficient Balance")
    def checkBalance(self):
        print("Current Balance Is : ",self.balance)

b1=Bank()
cname=input("Enter Customer Name : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)
    if choice==1:
        amount=int(input("Enter Deposite Amount : "))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkBalance()
        print("*"*50)
    elif choice==4:
        print("Thank You For Using Our Services.")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Please Try Agin.")
        print("*"*50)
    
