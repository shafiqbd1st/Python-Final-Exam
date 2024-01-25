import random
class Bank:
    __user_accounts = []
    __transaction_history = []
    __Total_balance = 0
    __Loan_amount = 0
    loan = True
    def __init__(self) -> None:
        pass
    
    def create_account(self,name, email, address, type):
        acc = len(Bank.__user_accounts) + 1001
        amount = 0
        loan = 0
        loan_amount = 0
        id = {"Account No:": acc, "Name:": name,  "Email:": email, "Address:": address, "Type:": type,
               "Balance:": amount, "Loan:": loan, "Loan_amount:": loan_amount}
        Bank.__user_accounts.append(id)
        return acc

    def deposit(self, acc, amount):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        for i in Bank.__user_accounts:
            for key, val in i.items():
                if val == acc:
                    ck = 1
                    i["Balance:"] = i["Balance:"] + amount
                    Bank.__Total_balance += amount
                    val =  {acc: {"Diposit": amount}}
                    Bank.__transaction_history.append(val)
                    return 1
            if ck == 1:
                break

        if ck == 0:
            print("Enter correct account")
            return 0
        print()
        
    def Transfer(self, acc, acc1, amount):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln < 2:
            print("Do not have more than one account in the bank")
            return 
        for i in Bank.__user_accounts:
            for key, val in i.items():
                if val == acc:
                    ck = 1
                    if amount < i["Balance:"]:
                        result = self.deposit(acc1, amount)
                        if result == 1:
                            i["Balance:"] = i["Balance:"] - amount
                            # Bank.__Total_balance -= amount
                            val =  {acc: {"Transfer": -amount}}
                            Bank.__transaction_history.append(val)
                        else:
                            print(f'{acc1} Is not valid account')
                    break
            if ck == 1:
                break
        if ck == 0:
            print("Enter correct account")
        print()

    def  Check_Balance(self, acc):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        for i in Bank.__user_accounts:
            for key, val in i.items():
                if val == acc:
                    ck = 1
                    print('Your total balance:', i["Balance:"])
                    break
            if ck == 1:
                break

        if ck == 0:
            print("Enter correct account")
        print()
        
    def withdraw(self, acc, amount):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        for i in Bank.__user_accounts:
            for key, val in i.items():
                if val == acc:
                    ck = 1
                    if i["Balance:"] < amount:
                        print('Please Enter less than', i["Balance:"]+1)
                    else:
                        i["Balance:"] = i["Balance:"] - amount
                        Bank.__Total_balance -= amount
                        val =  {acc: {"Withdrawal": -amount}}
                        Bank.__transaction_history.append(val)
                    break
            if ck == 1:
                break
        if ck == 0:
            print("Enter correct account")
        print()

    def Take_Loan(self, acc, amount):
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        elif amount > Bank.__Total_balance:
            print("Sorry! there is not enough money in the bank.")
        elif Bank.loan:
            ck = 0
            for i in Bank.__user_accounts:
                for key, val in i.items():
                    if val == acc:
                        ck = 1
                        v = i["Loan:"]
                        if v < 2:
                            i["Loan:"] += 1
                            i["Loan_amount:"] += amount
                            i["Balance:"] += amount
                            Bank.__Total_balance -= amount
                            Bank.__Loan_amount += amount
                            val =  {acc: {"Diposit": amount}}
                            Bank.__transaction_history.append(val)
                        else:
                            print("Sorry! You cannot loan at most two times.")
                        break
                if ck == 1:
                    break
            if ck == 0:
                print("Enter correct account")
        else:
            print('Cannot take loan from this bank')

        print()               

    def transaction_history(self, acc):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        for i in Bank.__transaction_history:
            for key, val in i.items():
                if key == acc:
                    ck = 1
                    print(val)
        if ck == 0:
            print("Enter correct account")
        print()            

    def Delete_account(self, acc):
        ck = 0
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        for i in Bank.__user_accounts:
            for key, val in i.items():
                if val == acc:
                    ck = 1
                    Bank.__Total_balance -= i["Balance:"]
                    Bank.__user_accounts.remove(i)
                    break
            if ck == 1:
                break

        if ck == 0:
            print("Enter correct account")
        print()

    def show_ALL_info(self):
        ln = len(Bank.__user_accounts)
        if ln == 0:
            print("No account has been opened in the bank till now")
            return 
        print("All bank account information is displayed")
        print()
        for i in Bank.__user_accounts:
            for key, val in i.items():
                print(key, val)
            print()
        print()

    def total_balance(self):
        total = 0
        for i in Bank.__user_accounts:
                total += i["Balance:"]
        print("Total balance: ", total)

    def total_loan_amount(self):
        total = 0
        for i in Bank.__user_accounts:
                total += i["Loan_amount:"]
        print("Total Loan amount: ", total)

    def on_of(self, val):
        if val == 1:
            print('ON the loan feature of the bank')
            Bank.loan = True
        else: 
            print('Off the loan feature of the bank')
            Bank.loan = False
                
class User(Bank):
    def __init__(self) -> None:
        super().__init__()
    
    def create_account(self, name, email, address, type):
        return super().create_account(name, email, address, type)
    
b = Bank()
a = User()
while(True):
    print("\t1. ADMIN")
    print("\t2. USER")
    print("\t3. EXIT")
    print()
    n = int(input("Enter your choice: "))
    if n == 1:
        print("ADMIN ID: admin ADMIN PASSWORD: 123")
        while(True):
            print()
            print("1. Create an account")
            print("2. Delete any user account")
            print("3. See all user accounts list ")
            print("4. Check the total available balance of the bank")
            print("5. Check the total loan amount.")
            print("6. On or Off the loan feature of the bank")
            print("7. Logout")
            x = int(input('Enter your choice: '))
            if x == 1:
                print("Please Enter your Info")
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                type = input("Savings Account or Current Account(s/c): ")
                id = a.create_account(name, email, address, type)
                print()
                print('Your account is create successfully')
                print('Your account no is: ', id)
            elif x == 2:
                acc = int(input('Enter accoutn No: '))
                b.Delete_account(acc)
            elif x == 3:
                b.show_ALL_info()
            elif x == 4:
                b.total_balance()
            elif x == 5:
                b.total_loan_amount()
            elif x == 6:
                print("1. ON")
                print("2. OFF")
                o = int(input('Enter your choice: '))
                b.on_of(o)
            elif x == 7:
                break 
    elif n == 2:
        while(True):
            print()
            print("1. Create an account")
            print("2. Doposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Check Transaction History")
            print("6. Take Loan")
            print("7. Transfer")
            print("8. Logout")
            print()
            x = int(input('Enter your choice: '))
            if x == 1:
                ch = input("Login or Register(L/R): ")
                if ch == 'R':
                    print("Please Enter your Info")
                    name = input("Name: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    type = input("Savings Account or Current Account(s/c): ")
                    id = a.create_account(name, email, address, type)
                    print()
                    print('Your account is create successfully')
                    print('Your account no is: ', id)
                elif ch == 'L':
                    while(True):
                        print()
                        print("1. Doposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take Loan")
                        print("6. Transfer")
                        print("7. Logout")
                        y = int(input('Enter your choice: '))
                        if y == 1:
                            acc = int(input('Enter your accoutn No: '))
                            amount = int(input('Enter amount: '))
                            if amount < 0:
                                print('Please enter the right amount')
                            else:
                                a.deposit(acc, amount) 
                        elif y == 2:
                            acc = int(input('Enter your accoutn No: '))
                            amount = int(input('Enter amount: '))
                            a.withdraw(acc, amount)
                        elif y == 3:
                            acc = int(input('Enter your accoutn No: '))
                            a.Check_Balance(acc)
                        elif y == 4:
                            acc = int(input('Enter your accoutn No: '))
                            a.transaction_history(acc)
                    
                        elif y == 5:
                            acc = int(input('Enter your accoutn No: '))
                            amount = int(input('Enter amount: '))
                            a.Take_Loan(acc, amount)
                        elif y == 6:
                            acc = int(input('Enter your accoutn No: '))
                            acc1 = int(input('Enter Transfer accoutn No: '))
                            amount = int(input('Enter amount: '))
                            a.Transfer(acc, acc1, amount)
                        elif y == 7: 
                            break
            if x == 2:
                acc = int(input('Enter your accoutn No: '))
                amount = int(input('Enter amount: '))
                if amount < 0:
                    print('Please enter the right amount')
                else:
                    a.deposit(acc, amount) 
            elif x == 3:
                acc = int(input('Enter your accoutn No: '))
                amount = int(input('Enter amount: '))
                a.withdraw(acc, amount)
            elif x == 4:
                acc = int(input('Enter your accoutn No: '))
                a.Check_Balance(acc)
            elif x == 5:
                acc = int(input('Enter your accoutn No: '))
                a.transaction_history(acc)
            elif x == 6:
                acc = int(input('Enter your accoutn No: '))
                amount = int(input('Enter amount: '))
                a.Take_Loan(acc, amount)
            elif x == 7:
                acc = int(input('Enter your accoutn No: '))
                acc1 = int(input('Enter Transfer accoutn No: '))
                amount = int(input('Enter amount: '))
                a.Transfer(acc, acc1, amount)
            elif x == 8: 
                break
    if n == 3:
        break
