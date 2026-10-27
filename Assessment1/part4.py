
#Class
class Student:
 def __init__(self,name,roll_number, marks):
    self.name= name
    self.roll_number = roll_number
    self.marks = marks
     
 def display_details(self):
    print(self.name, self.roll_number, self.marks)

 def check_details(self) :
  if self.marks >=40:
    return "PASS"
  else:
     return "FAIL"

Student1 = Student("carline",232, 40) 
Student2 = Student("Prisilla",232, 10)  

stud =[Student1,Student2]   
for ss in stud:
 ss.display_details() 
 print(ss.check_details())
   
   
  
     
        