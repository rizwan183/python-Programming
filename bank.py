import sqlite3 as s
conn=s.connect("bank.db")
cor=conn.cursor()
def bank():
        try:
            cor.execute("create table Acc_det (ac_no number primary key ,name text,pin number,balance real)")
        except:
            print("__________________________Menu___________________________________")
            print("1 Add New Acc")
            print("2 View All Acc")
            print("3 Delete One Acc")
            print("4 update One Acc")
            ch = int(input("Select Any One Option"))
            if ch == 1:
                ac = int(input("Enter Acc No"))
                cor.execute("select ac_no from Acc_det where ac_no=?", (ac,))
                res = cor.fetchone()
                if res == None:
                    name = input("Enter Name ")
                    pin = int(input("enter pin"))
                    bal = float(input("enter balance"))
                    cor.execute("insert into Acc_det values(?,?,?,?)", (ac, name, pin, bal))
                    conn.commit()
                    print("Data SuccessFully Added")
                else:
                    print("Ac Is Already In Account")
            elif ch == 2:
                cor.execute("select *from Acc_det")
                res = cor.fetchall()
                print(res)
            elif ch == 3:
                ac = int(input("Enter Acc No"))
                cor.execute("select ac_no from Acc_det where ac_no=?", (ac,))
                res = cor.fetchone()
                if res != None:
                    cor.execute("delete from Acc_det where ac_no=?", (ac,))
                    conn.commit()
                    print(ac, "is success fully Deleted")
                else:
                    print(ac, "Is not found ")
            elif ch == 4:
                ac = int(input("Enter Acc No"))
                cor.execute("select ac_no from Acc_det where ac_no=?", (ac,))
                res = cor.fetchone()
                if res != None:
                    bal = float(input("enter balance"))
                    cor.execute("update Acc_det set balance=? where ac_no=?", (bal, ac))
                    conn.commit()
                    print("Balance is successfull Updated")
                else:
                    print("acc Not found")
            else:
                print("Wrong Choice Try Again ")

bank()





