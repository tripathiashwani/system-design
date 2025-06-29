class Employee:
    company = "TechCorp"    # class variable (static variable)

    def __init__(self, name):
        self.name = name


e1 = Employee("Ashwani")
e2 = Employee("Nikita")

print(e1.company)   # TechCorp
print(e2.company)   # TechCorp

Employee.company = "Innotech"
print(e1.company)   # Innotech
print(e2.company)   # Innotech



class parent:

    wealth=20097

    @staticmethod
    def s_method_parent():
        print("this is static method in parent class")


    

    

   


class child(parent):

    def __init__(self,childname):
        self.name=childname

    def get_wealth(self):

        print("get_wealth",self.wealth)

c=child("ashwani")
print("c.wealth",c.wealth)
c.get_wealth()
p=parent()

if p.wealth:
    print("parent class have wealth",p.wealth)
        
