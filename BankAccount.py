class BankAccount:
    bank_name ="Big Bank Roll"
    all_accounts = []
    def __init__(self, name, interest_rate, balance):
        self.name = name
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def add_deposit(self, amount):
        self.balance += amount
        #self.display_account()
        return self

    def make_withdraw(self,amount):
        
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance -= amount
        return self

    def display_account(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
# increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
            print(f"The account total is ${sum}")
        return sum



#To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info 
# all in one line of code (i.e. chaining)
ashley = BankAccount("Ashley", 0.04, 700 )
ashley.add_deposit(4500).add_deposit(7220).add_deposit(990).make_withdraw(100).yield_interest().display_account()
#print(ashley)

#To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all 
# in one line of code (i.e. chaining)

creed = BankAccount("creed", 0.05, 0)
creed.add_deposit(500).add_deposit(220).add_deposit(990).make_withdraw(480).yield_interest().display_account()
#print(creed)

#Bonus
BankAccount.all_balances()