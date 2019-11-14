class Employee:
    company = "Love Python"
    def __init__(self, position, salary, name, surname,  seniority, e_mail, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.e_mail = e_mail
        self.is_student = is_student

    def salary_bump (self):
        self.salary *=1.07
        return self.salary
    def tax(self):
        return self.salary *0.02
    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary*proc
    def employee_email(self):
        primary = self.name +"."+self.surname
        secondary = self.company.replace(" ","").lower() +".com"
        email = primary + "@" + secondary
        return email

p1 = Employee("programista",5500,"Jan", "Kowalski",3, False)
print(p1.name)
print
print(p1.salary)
print(p1.salary_bump)
print(p1.salary)


