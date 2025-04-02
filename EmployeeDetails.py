class Employee:
    def __init__(self,name,id,salary,department):
        self.name=name
        self.id=id
        self.salary=salary
        self.department=department
    def calculate_salary(self,salary,hours_worked):
        overtime=0
        if hours_worked>50:
            overtime=hours_worked-50
        self.salary=self.salary+(overtime*(self.salary/50))
    def assign_department(self,emp_department):
        self.department=emp_department
    def print_employee_details(self):
        print("\nName:",self.name,end=' ')
        print("ID:",self.id,end=' ')
        print("Salary:",self.salary,end=' ')
        print("Department:",self.department,end=' ')

employee1=Employee("ASHWIN","AI876",50000,"ACCOUNTING")
employee2=Employee("PRABHU","AI499",45000,"RESEARCH")
employee3=Employee("SUDHAN","AI900",50000,"SALES")
employee4=Employee("DHATRI","AI698",55000,"OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

employee3.assign_department("JOURNALIST")
employee4.assign_department("DEVELOPER")

employee2.calculate_salary(45000,54)
employee4.calculate_salary(55000,60)

print("\n\nUpdated Employee Details:",end='')
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
