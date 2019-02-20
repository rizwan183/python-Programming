class Student:
    def assing(self):
        self.roll_no = int(input("Enter Roll_no !"))
        self.name =input("name")
        self.english = int(input("English Mark"))
        self.math = int(input("Math Mark"))
        self.science =int(input("Science Mark"))
    def dis(self):
        total = self.english + self.math + self.science
        print("Totoal Number is ", total)
        print("Percentage is ", total / 3)
print( "____________________________________________________________________________________________________________________")
s = Student()
s.assing()
s.dis()
s.assing()
s.dis()
s.assing()
s.dis()
s.assing()
s.dis()
s.assing()
s.dis()
