import csv
import os
def write():
    f = open('banking.csv','w',newline="")
    s_writer = csv.writer(f)
    s_writer.writerow(['Username','Password','Age','Gender','Balance'])
    f.close()

def append(new_user):
    f = open('banking.csv','a',newline="")
    s_writer = csv.writer(f)
    s_writer.writerow(new_user)
    f.close()

def read():
    f = open('banking.csv','r')
    s_reader = csv.reader(f)
    for i in s_reader:
        print(i)
    f.close()
def search(username):
    f = open('banking.csv','r')
    s_reader = csv.reader(f)
    for i in s_reader:
        if i[0]==username:
            return i
    f.close()

def update(username,balance):
    new_user_list = []
    file = open('banking.csv','r')
    reader = csv.reader(file)
    for i in reader:
        if i[0]==username:
            i[4] = float(balance)
        new_user_list.append(i)
    file.close()
    f = open('banking.csv','w+',newline='')
    writer = csv.writer(f)
    writer.writerows(new_user_list)
    f.close()
class User():
    def __init__(self,username,password,age,gender):
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
    def show_details(self):
        print('Personal Details')
        print(f'Name,{self.username}')
        print(f'Age,{self.age}')
        print(f'Gender,{self.gender}')

class Bank(User):
    def __init__(self,username,password,age,gender):
        super().__init__(username,password,age,gender)
        self.balance = 0
    def Signup(self):
        append([self.username,self.password,self.age,self.gender,self.balance])
        print('Hurray!! Welcome To Our Bank --')
    def change_balance_in_file(self,balance):
        update(self.username,balance)
    def deposit_for_first_time(self,deposit_amount):  
        self.balance = self.balance + deposit_amount
        print(f'Your Account Balance is {self.balance}')
    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f'Your Account Balance is {self.balance}')
        self.change_balance_in_file(self.balance)
    def withdraw(self,widhtdraw_amount):
        if widhtdraw_amount>self.balance:
            print(f'Insufficient Balance | Balance Availabe : {self.balance}')
        else:
            self.balance = self.balance - widhtdraw_amount
            print(f'Your Account Balance is {self.balance}')
            self.change_balance_in_file(self.balance)
    def view_balance(self):
        print(f'Your Account Balance is {self.balance}') 


        
username = input('Enter Your Username:')
password = input('Enter Your Password:')
def login():
    if password == search(username)[1]:
        print('Login Succesful')
        return True

def Check_User():
    f = open('banking.csv','r')
    s_reader = csv.reader(f)
    for i in s_reader:
        if i[0]==username:
            return True
    f.close()

if os.path.exists('banking.csv'):
    pass
else:
    write()
if Check_User():
    print('Welcome Back User Hope You Are Doing Well')
    if login():
        User = Bank(username,password,int(search(username)[2]),search(username)[3])
        User.deposit(float(search(username)[4]))
    else:
        print('Password Is Invalid Retry')
else:
    age = int(input('Enter Your Age:'))
    gender = input('Enter Your Gender:')
    User = Bank(username,password,age,gender)
    amount_to_deposit = float(input('Enter Amount To Deposit:'))
    User.deposit_for_first_time(amount_to_deposit)
    User.Signup()

while True:
    print('''
1.VIEW BALANCE
2.DEPOSIT
3.WITHDRAW
4.EXIT   
    ''')
    ch = int(input('Enter Your Choice:'))
    if ch==1:
        User.view_balance()
    elif ch==2:
        amount_to_deposit = float(input('Enter The Amount You Want To Deposit:'))
        User.deposit(amount_to_deposit)
    elif ch==3:
        amount_to_withdraw = float(input('Enter The Amount You Want To WithDraw:'))
        User.withdraw(amount_to_withdraw)
    elif ch==4:
        print('Thank You')
        exit()

    
    

