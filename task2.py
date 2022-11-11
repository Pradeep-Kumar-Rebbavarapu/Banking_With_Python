import csv
def write():
    
    users_username = input('Enter Your Username:')
    users_password = input('Enter Your Password:')
   

class Bank:
    Users = []
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def Signup(self):
        f = open('textfile1.txt','a')
        list1 = [self.username + ' : ',self.password + '\n']
        f.writelines(list1)
        f.close()
    def Login(self):
        pass
    def Deposit_Money(self):
        pass
    def Send_Money(self):
        pass
    def Check_Balance(self):
        pass
    def Withdraw_Money(self):
        pass
    def Print_User_Details(self):
        return f'your username is {self.username},your password is {self.password} and your balance is {self.balance} Rs'


username = input('Enter Your Username:')
password = input('Enter Your Password:')
User = Bank(username,password)
User.Signup()
        