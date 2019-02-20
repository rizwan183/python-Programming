class Bank_Account:
    def assing(self,deposittor_name,acc_no,acc_type,bal):
        self.name=deposittor_name
        self.acc_num=acc_no
        self.acc_type=acc_type
        self.balance=bal
    def acc_det(self):
        print("Name ! ",self.name)
        print("Account Number !",self.acc_num)
        print("Account Type",self.acc_type)
        print("Available Balance",self.balance)
    def deposit(self,dep):
        self.balance=dep+self.balance
        print("After Deposit Your Current Available Balance Is ! ",self.balance)
    def withDrwa(self,withd):
        self.balance=self.balance-withd
        print("After WithDraw Your Current Available Balance Is ! ", self.balance)
    def dip(self):
        print("Name ",self.name)
        print("Available Balance",self.balance)
print("____________________________________________________________________________________________________________________")
print("___________________________________Enter Account Details____________________________________________________________")
name=input("Enter Depositor name! ")
acc_no=int(input("Enter Acc No !"))
acc_type=input("enter acc type !")
balance=float(input("Enter Balance"))
b=Bank_Account()
b.assing(name,acc_no,acc_type,balance)
print("____________________________________________________________________________________________________________________")
print("___________________________________Account Details__________________________________________________________________")
b.acc_det()
print("____________________________________________________________________________________________________________________")
print("___________________________________Deposit__________________________________________________________________________")
dep=float(input("Enter Deposit Amount"))
b.deposit(dep)
print("____________________________________________________________________________________________________________________")
print("___________________________________WithDrwa__________________________________________________________________________")
withd=float(input("Enter Withdraw Amount"))
b.withDrwa(withd)
print("____________________________________________________________________________________________________________")
b.dip()
