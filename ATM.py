import os
DATA_File='users.txt'

def load_data():
    users={}
    if os.path.exists(DATA_File):
        with open(DATA_File,'r') as f:
            for line in f:
                if line:
                    line=line.strip()
                    pin,bal=line.split(',')
    return users                

def save_user(users):
    with open(DATA_File,'w') as f:
        for pin,bal in users.items():
            f.write(f'{pin},{bal}\n')
    
def show():
    print('')
    print('1.withdraw\n')
    print('2.deposit\n')
    print('3.balance check\n')
    print('4.Exit\n')
def run(users,pin):
    while True:
        show()
        ch=int(input("Enter the choice:"))
        if ch==1:
            withdraw(users,pin)
        elif ch==2:
            deposit(users,pin)
        elif ch==3:
            bal_check(users,pin)
        elif ch==4:
            print("thank you")
            break
        else:
            print('Invalid option')
            
def withdraw(users,pin):
    
    amt=int(input("Enter the amount:"))
    if amt<=users[pin]:
        users[pin]-=amt
        print(f'Current Balance:{users[pin]}\nWithdraw amount:{amt}')
        save_user(users)
    else:
        print("Insufficient amount")
    
    
def deposit(users,pin):
    
    amt=int(input("Enter the amount:"))
    users[pin]+=amt
    print(f'Current Balance:{users[pin]}\nDeposit amount:{amt}')
    save_user(users)
    
def bal_check(users,pin):
    print("current balance:",users[pin])
    
def main():
    users=load_data()
    p=int(input("Enter the pin:"))
    if p not in users:
        print("Pin not found creating new account........")
        users[p]=0.0
        save_user(users)
    run(users,p)
        
if __name__=="__main__":
    main()
