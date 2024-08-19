class Company:
    companyName = "Apple"

    def show(self):
        print(f"Company name is {self.companyName} and My name is {self.name}")

# class methods are added with decorator name @classmethod
    @classmethod
    def changeCompany(cls, change):
        cls.companyName = change


e1 = Company()
e1.name = "Saurabh"
e1.show()
e1.changeCompany("Adidas")
e1.show()
print(Company.companyName)
