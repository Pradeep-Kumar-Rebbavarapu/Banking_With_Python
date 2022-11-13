from datetime import date
import csv
import os
import random
import datetime
x = datetime.datetime.now()


def getdate():
    today = date.today()
    day = 23
    mydate = datetime.datetime.now()
    month = mydate.strftime("%B")
    year = today.year
    if day == 1 or day == 21 or day == 31:
        current_day = f"{day}st {month} {year}"
    elif day == 3 or day == 23:
        current_day = f"{day}rd {month} {year}"
    else:
        current_day = f"{day}th {month} {year}"
    return current_day


def gettime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time[0:2])
    if hour > 12:
        new_time = str(hour - 12) + current_time[2:] + ' pm'
    elif hour == 0:
        new_time = str(12) + current_time[2:] + ' am'
    elif hour < 12:
        new_time = str(hour) + current_time[2:] + ' am'
    elif hour == 12:
        new_time = str(12) + current_time[2:] + ' pm'
    return new_time


def write():
    f = open('banking.csv', 'w', newline="")
    s_writer = csv.writer(f)
    s_writer.writerow(['Username', 'Password', 'Age', 'Gender', 'Balance'])
    f.close()
    
def make_user_file(username,age):
    r = open(f'{username}-{age}.csv', 'w', newline="")
    writer = csv.writer(r)
    writer.writerow([' DATE ', ' TIME ', ' AMOUNT ',' TYPE ', ' ACCOUNT NAME '])
    r.close()

def append(new_user, file_name):
    f = open(file_name, 'a', newline="")
    s_writer = csv.writer(f)
    s_writer.writerow(new_user)
    f.close()


def read():
    f = open('banking.csv', 'r')
    s_reader = csv.reader(f)
    for i in s_reader:
        print(i)
    f.close()


def search(username):
    f = open('banking.csv', 'r')
    s_reader = csv.reader(f)
    k = []
    for i in s_reader:

        if i[0] == username:
            k = i
            break
    f.close()
    return k


def update(username, balance):
    new_user_list = []
    file = open('banking.csv', 'r')
    reader = csv.reader(file)
    for i in reader:
        if i[0] == username:
            i[4] = float(balance)
        new_user_list.append(i)
    file.close()
    f = open('banking.csv', 'w+', newline='')
    writer = csv.writer(f)
    writer.writerows(new_user_list)
    f.close()


class User():
    def __init__(self, username, password, age, gender):
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Details')
        print(f'NAME : {self.username}')
        print(f'AGE : {self.age}')
        print(f'GENDER : {self.gender}')
        print(f'BANK ID : {self.make_bank_id()}')
        print(f'BANK BALANCE : {self.balance}')


class Bank(User):
    def __init__(self, username, password, age, gender):
        super().__init__(username, password, age, gender)
        self.balance = 0

    def make_bank_id(self):
        return f'{self.username}{random.random()}{self.age}{random.random()}{x}'

    def Signup(self):
        append([self.username, self.password, self.age,
               self.gender, self.balance], 'banking.csv')
        print('Hurray!! Welcome To Our Bank --')
        print("===============================")

    def transaction_history(self, amount, type_of_transaction, account_name):
        append([getdate(), gettime(), amount, type_of_transaction,account_name], f'{self.username}-{self.age}.csv')

    def change_balance_in_file(self, balance):
        update(self.username, balance)

    def deposit_for_first_time(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f'TRANSACTION SUCCESFUL')
        print("===============================")
        self.transaction_history(deposit_amount, 'DEPOSITED BY', self.username)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        self.change_balance_in_file(self.balance)
        self.transaction_history(deposit_amount, 'DEPOSITED BY', self.username)

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(f'Insufficient Balance | Balance Availabe : {self.balance}')
            print("===============================")
        else:
            self.balance = self.balance - withdraw_amount
            print(f'Your Account Balance is {self.balance}')
            print("===============================")
            self.change_balance_in_file(self.balance)
        self.transaction_history(withdraw_amount, 'WITHDRAWN BY', self.username)

    def transfer_amount(self):
        user_to_be_transfered = input('Enter The Username Of The User You Want To Transfer Money To:')
        print("===============================")
        amount_to_be_transfered = float(input('Enter The AMOUNT You Want to Transfer:'))
        print("===============================")
        if self.balance < amount_to_be_transfered:
            print('Insufficient Balance')
        else:
            k = search(user_to_be_transfered)
            k[4] = float(k[4]) + amount_to_be_transfered
            update(user_to_be_transfered, k[4])
            self.balance = self.balance - amount_to_be_transfered
            update(self.username, self.balance)
        other_persons_age = search(user_to_be_transfered)[2]
        self.transaction_history(amount_to_be_transfered, 'TRANSFERED TO', user_to_be_transfered)
        append([getdate(), gettime(),amount_to_be_transfered, 'DEPOSITED FROM',self.username], f'{user_to_be_transfered}-{other_persons_age}.csv')
    def get_transaction_history(self):
        f = open(f'{self.username}-{self.age}.csv','r')
        for i in f:
            print("===============================")
            print(i)
            print("===============================")
    def view_balance(self):
        print(f'Your Account Balance is {self.balance}')

print("===============================")
username = input('Enter Your Username:')
print("===============================")
password = input('Enter Your Password:')
print("===============================")


def login():
    if password == search(username)[1]:
        return True
    else:
        return False


def Check_User():
    f = open('banking.csv', 'r')
    s_reader = csv.reader(f)
    for i in s_reader:
        if i[0] == username:
            return True
    f.close()

if os.path.exists('banking.csv'):
        pass
else:
        write()
if Check_User():
        print('Welcome Back User Hope You Are Doing Well')
        print("===============================")
        if login():
            User = Bank(username,password,int(search(username)[2]),search(username)[3])
            User.deposit(float(search(username)[4]))
        else:
            print('Password Is Invalid Retry')
                
else:
        
        age = int(input('Enter Your Age:'))
        print("===============================")
        gender = input('Enter Your Gender:')
        print("===============================")
        make_user_file(username,age)
        User = Bank(username,password,age,gender)
        amount_to_deposit = float(input('Enter Amount To Deposit:'))
        print("===============================")
        User.deposit_for_first_time(amount_to_deposit)
        User.Signup()

while True:
    
    
    print('''
=====================
1.VIEW YOUR DETAILS
2.VIEW BALANCE
3.DEPOSIT
4.WITHDRAW
5.TRANSFER MONEY
6.GET TRANSACTION HISTORY
7.EXIT
=====================   
    ''')
    ch = int(input('Enter Your Choice:'))
    print("===============================")
    if ch==1:
        User.show_details()
    elif ch==2:
        User.view_balance()
    elif ch==3:
        amount_to_deposit = float(input('Enter The Amount You Want To Deposit:'))
        print("===============================")
        User.deposit(amount_to_deposit)
    elif ch==4:
        amount_to_withdraw = float(input('Enter The Amount You Want To WithDraw:'))
        User.withdraw(amount_to_withdraw)
    elif ch==5:
        User.transfer_amount()
    elif ch==6:
        User.get_transaction_history()
    elif ch==7:
        exit()



    
    

