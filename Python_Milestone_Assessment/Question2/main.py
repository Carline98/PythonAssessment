class employee:
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_salary=emp_salary

    def read_employee(filename='employees.txt'):
        employees = []
        try:
            with open(filename,'r') as r:
                for details in r:
                    emp_id,emp_name,emp_role,emp_salary=details.strip().split(",")
                    employees.append(employee(emp_id,emp_name,emp_role,int(emp_salary)))
        #print (employees    ) 
        except FileNotFoundError:
            print(f"file '{filename}' not found")
        return employees  
    
    def add_employee(emp_id,emp_name,emp_role,emp_salary,filename='employees.txt'):
            with open (filename,"a") as r:
                r.write(f"{emp_id},{emp_name},{emp_role},{emp_salary}\n") 
            
    def display_details(self):        
        print(f"{self.emp_id}- {self.emp_name}- {self.emp_role}- ₹{self.emp_salary}")

    def find_highest_salary(employees):
        return max(employees, key=lambda e:e.emp_salary)

    def rolecount(employees):
        counts={}
        for e in employees:
            counts[e.emp_role] =counts.get(e.emp_role,0)+1
        return counts
    


employees =employee. read_employee()
#employee.add_employee(104,"carlinejk","Developer",66000)

print("-----Employee Details-----")
for e in   employees:      
    e.display_details()

print("-----Employee with salary>5000-----")    
for e in   employees:
    if e.emp_salary>50000:
        
        print(f"{e.emp_name} - ₹{e.emp_salary}")
high = employee.find_highest_salary(employees)
print(f"The highest paid employee: {high.emp_name} - ₹{high.emp_salary}")   

for emp_role, rolecount in sorted(employee.rolecount(employees).items()):
    print(f"{emp_role} - {rolecount}")





