# _______________________________________________________Example of Single Inheritance______________________________________________
class Student:
    # name=""
    # roll=0
    # course=""
    # section=""
    # address=""
    def info(self):
        name=input("Enter Student Name: ")
        roll=int(input("Enter Student Roll No: "))
        course=input("Enter Student Course Name: ")
        section=input("Enter Student Section: ")
        address=input("Enter Student Address: ")
    def disp(self):
        print("Student Name: ",self.name)
        print("Student Roll No: ",self.roll)
        print("Student Course: ",self.course)
        print("Student Section: ",self.section)
        print("Student Address: ",self.address)
s=Student()
s.info()
s.disp()

# _______________________________________________________Example of Single Inheritance______________________________________________
# class Abc:
#     def fun(self):
#         print("Hii")
# class Xyz(Abc):
#     def fun2(self):
#         print("Hello")
# obj=Xyz()
# obj.fun()
# obj.fun2()