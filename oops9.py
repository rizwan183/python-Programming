from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://rizwan-python.firebaseio.com/")
class Student:
    core = 3000
    advance = 3500
    tax=12.3
    def Payment(self):
        if self.choice==1:
            if(self.paid<Student.core):
                self.rem=Student.core-self.paid
                self.rem1=(Student.tax/100)*self.paid

            self.d1={
                "Roll_Num":self.roll_no,
                "Name":self.name,
                "Course":"Core Python",
                "Course_Fee":Student.core,
                "Paid":self.paid,
                "Remaining_Fee":self.rem,
                "Late Fee":self.rem1
            }
            fire.put("Rizwan","Student",self.d1)
            print("Your SuccessFully Registered For Core Python")
        elif self.choice==2:
            if (self.paid < Student.advance):
                self.rem =Student.advance-self.paid
                self.rem1 = (Student.tax / 100) * self.paid
            self.d1 = {
                "Roll_Num": self.roll_no,
                "Name": self.name,
                "Course": "Advance Python",
                "Course_Fee": Student.advance,
                "Paid":self.paid,
                "Remaining_Fee":self.rem,
                "Late Fee":self.rem1

            }
            fire.put("Rizwan", "Student", self.d1)
            print("Your SuccessFully Registered For Advance Python")
        else:
            print("Wrong Choice")
    def __init__(self):
        self.roll_no = int(input("Enter Roll Number! "))
        self.name = input("Enter Name! ")
        print("Which Course U Want To Join 1)core Python=3000 2)Advance Python=3500")
        self.choice = int(input("Enter Your Course Number"))
        self.paid = int(input("Pay Amount"))
        self.Payment()
        res=fire.get("Rizwan","Student")
        print(res)
Student()
