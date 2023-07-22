# _______________________________________________________Class & Object in Python______________________________________________
class Hello:
    l=0
    b=0
    def area(self):
        ar=self.l*self.b
        print("Area of Rectangle=",ar)
    # def area(l,b):
    #     ar=l*b
    #     print("Area of Rectangle=",ar)
h=Hello()
# l=float(input("Enter The Length of Rectangle: "))
# b=float(input("Enter The Breadth of Rectangle: "))
h.l=5.5
h.b=4.4
h.area()

# _______________________________________________________Example of Class & Object______________________________________________
# class Employee:
#     name=""
#     department=""
#     salary=""
#     def emp(self):
#         print("EmpName: ",self.name)
#         print("DptName: ",self.department)
#         print("Salary: ",self.salary)
# e=Employee()
# e.name='Vivek Kumar'
# e.department='Software Engineering'
# e.salary=210000
# e.emp()