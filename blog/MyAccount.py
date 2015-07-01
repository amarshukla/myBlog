class MyAccount(object):
    def __init__(self, holder, number, balance, credit_line=1500):
        self.holder = holder
        self.number = number
        self.balance = balance
        self.creditLine = credit_line

    def deposit(self,amount):
        self.balance += amount
        print "deposited Rs %d and new balance is %d" %amount %self.balance

    def withdraw(self, amount):
        if self.balance - amount < self.creditLine:
            print "minimum balance has to be maintained so withdrawl is not possible"
        else:
            self.balance -= amount
            print "your account is debited with Rs %d and new account balance is %d" %amount %self.balance
            