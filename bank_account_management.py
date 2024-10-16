class BankAccount():
    defaultAccNumber = 1000129399001      

    def __init__(self, user, balance = 0):
        self.user = user
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, dep):
        self.balance += dep
        print(f"{dep}PKR is successfully deposit into your account\nYour current Balance is {self.balance}")

    def withdraw(self, wit):
        
        if self.balance < wit:
            print('Not enough balance!')
        else:
            self.balance -= wit
            print(f"\n{wit}PKR is successfully withdraw from your account\nYour current Balance is {self.balance}")

    def getBalance(self):
        return self.balance
    
    def showDetails(self):
        print("\n*********** Welcome to Sheikh Bank ***********")
        while True:
            operations = int(input(f"\nPlease Choose any number 1 to 5 to perform action: \nEnter 1 to Deposit money \nEnter 2 to Withdraw money \nEnter 3 to Check balance \nEnter 4 to Create new Account \nEnter 5 to Exit/Close\nChoose Number: "))
            
            if operations == 1:
                dep = int(input("\nHow much money you want to deposit: "))
                self.deposit(dep)
            
            elif operations == 2:
                wit = int(input(f"\nHow much money you want to withdraw: "))
                self.withdraw(wit) 
                
            elif operations == 3:
                print(f"\nAccount Holder Name: {self.user}")
                print(f"Account Number: {self.defaultAccNumber}")
                print(f"Account Balance: {self.balance}")

            elif operations == 4:
                print("\n*********** Welcome to Sheikh Bank ***********\n")
                self.user = input("Enter Your name: ")
                self.balance = int(input("Deposit money to open your account: "))
                self.user1 = BankAccount(self.user,self.balance)
                print(f"\nCongratulation {self.user}, \nYour account created Succesfully \nYour Account Number is {self.defaultAccNumber} \nYour available balance is {self.user1.getBalance()}")
            
            elif operations == 5:
                print("\nProgram Successfully stopped......")
                break
            
            else:
                print("\nInvalid Action!\nPlease choose right number between 1 to 5")
        

            
            
       
defaul_user = BankAccount("yousuf", 500)
defaul_user.showDetails()

