#23/08/25
#getters and setters

class fruit():
    def __init__(self,name,shape,taste,CoO,color):
        self.name = name
        self.shape = shape
        self.taste = taste
        self.__CoO = CoO
        self.color = color
    def private(self):
        return self.__CoO
    def setting(self,coo):
        self.__CoO = coo
    def printer(self):
        print(f'name: {self.name}, shape: {self.shape}, taste: {self.taste}, color: {self.color}')
    
'''green_apple = fruit('green apple','spherical','sweet','uk','green')
green_apple.printer()
print(green_apple.private())

green_apple.setting('japan')
print(green_apple.private())
'''
class bank():
    def __init__(self,account_holder,default_pin='0000',balance = 0):
        self.account_holder = account_holder
        self.__default_pin = default_pin
        self.balance = balance

    def check_b(self):
        return f"{self.account_holder}'s balance: {self.balance}"
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return f'{amount} deposited successfully'
        else:
            return 'Error... Please deposit a valid amount'
    def withdrawl(self,amount):
        if self.balance > 0:
            self.balance-=amount
            return 'Successful withdrawl'
        else:
            return 'Insufficient funds'
        
    def __validate(self,input_pin):
        return input_pin == self.__default_pin
    def enterPin(self):
        input_pin = input('enter PIN')

        return self.__validate(input_pin)

myBank = bank('Yash Patro','1234',200)
if myBank.enterPin():
    print('Menu \n1.Check Balance\n2.deposit\n3.withdrawl')
    user_input = int(input('Pick an option by writing the corresponding number'))
    if user_input == 1:
        print(myBank.check_b())
    elif user_input == 2:
        desposit_a = int(input('Enter the deposit amount'))
        print(myBank.deposit(desposit_a))
        print(myBank.check_b())
    elif user_input == 3:
        withdrawl_a = int(input('Enter the withdrawl amount'))
        print(myBank.withdrawl(withdrawl_a))
        print(myBank.check_b())
    else:
        print('Invalid input')

else:
    print('Incorrect PIN, Try again')
