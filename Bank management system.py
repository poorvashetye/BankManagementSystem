from random import randint
print('Welcome to Bank Management System')
print('1->Create Account 2->Withdrawal 3->Deposit')
a=input('Choose the operation to perform(1/2/3)')
def create():
    print('Welcome To create account section')
    fname=input('Enter Your First Name')
    mname=input('Enter Your Middle Name')
    lname=input('Enter Your Last Name')
    acc_type=input('Enter The Account Type to open(1/2) 1->Savings 2->Current')
    bdate=input('Enter Your Birth date')
    pno=input('Enter Your Mobile Number')
    pan=input('Enter Your Pan Card Number')
    aad=input('Enter Your Aadhar Card Number')
    num=input('Enter any key to create an account')
    print('Account Created Successfully')
    print('Account details are as follows:-')
    n = 10
    range_start = 10**(n-1)
    range_end = (10**n)-1
    global n1
    n1 = randint(range_start, range_end)
    print('Your Details Are:-')
    print('Account Number:-',n1)
    print('Name:-',fname+' '+mname+' '+lname)
    if acc_type == '1':
        print('Account Type:- Savings')
    else:
        print('Account Type:- Current')
    print('Birth Date:-',bdate)
    print('Mobile Number:-',pno)
    print('Pan Card Number:-',pan)
    print('Aadhar Card Number:-',aad)
if a == '1':
    create()
elif a == '2':
    b=input('Do You Have Account in the bank 1->Yes 2->No')
    if b == '1':
        acc1=input('Enter Your Account Number:-')
        op=input('Enter Your Opening Balance:-')
        o=int(op)
        withdrawa1=input('Enter The amount to withdraw from the account')
        with1=int(withdrawal)
        if(with1 > o):
            print('Insufficient Balance')
        else:
            print(with1+'Withdrawed from the account')
            print('Remaining Balance:-'+int(o-with1))
    else:
        create()
        op1 = input('Enter Your Opening Balance')
        op5=int(op1)
        withdraw= input('Enter The amount to withdraw from the account')
        with2=int(withdraw)
        if(with2 > op5):
            print('Insufficient Balance')
        else:
            bal1=op5-with2
            bal2=int(bal1)
            print('Remaining Balance:-')
            print(bal2)
elif a == '3':
    c=input('Do You Have Account in the bank 1->Yes 2->No')
    if c== "1":
        print('Enter Account Number:-')
        op2=input('Enter Your Opening Balance')
        deposit1=input('Enter the amount to deposit in the account')
        print(deposit+'deposited in the account')
        print('Balance:-'+op2+deposit1)
    else:
        create()
        op3=input('Enter Your Opening Balance')
        op6=int(op3)
        deposit=input('Enter the amount to deposit in the account')
        depo2=int(deposit)
        bal3 = (op6) + (depo2)
        bal4=int(bal3)
        print('Balance:- {}'.format(bal4))
else:
    print('Wrong Choice')
            
