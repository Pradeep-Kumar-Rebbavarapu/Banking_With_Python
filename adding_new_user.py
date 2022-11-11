import pickle

def write():
    f = open("BinaryWrite.dat","wb")
    dict1 = [['Pradeep',1234],['Pavan',98765]]
    pickle.dump(dict1,f)
    f.close()
def Append():
    f = open("BinaryWrite.dat","ab")
    dict1 = [['PCUwwwww',12345]]
    pickle.dump(dict1,f)
    f.close()
def read():
    f = open("BinaryWrite.dat","rb")
    while True:
        try:
            s = pickle.load(f)
            for i in s:
                print(i)
        except Exception as e:
            break
    
    f.close()
def search(name):
    found = False
    f  = open("BinaryWrite.dat","rb")
    s = pickle.load(f)
    for i in s:
        if i[0]==name:
            print(i)
            found = True
    if found == False:
        print('Record Not Found')
def update(username):
    f  = open("BinaryWrite.dat","rb+")
    s = pickle.load(f)
    found = False
    for i in s:
        if i[0]==username:
            print(f'Current name is : {i[0]}')
            i[0] = input("Enter New Name:")
            found = True
            break
    if found == False:
        print('User Not Found')
    else:
        f.seek(0)
        pickle.dump(s,f)
    f.close()
write()
Append()
read()
# update('Pradeep')

