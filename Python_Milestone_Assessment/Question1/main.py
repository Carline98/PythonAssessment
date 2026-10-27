def grade(avg):
    if avg>=90:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=50:
        return "C"
    elif avg>=40:
        return "D"
    else:
        return "F"
    
def result(avg):
    if avg>=40:
        return "PASS"
    else:
        return "FAIL"
print("-----Student Details-----")    
Students = []
n = int(input("The Number of Students: "))
for i in range(n):
    sid=input("Student ID: ")
    name= input("Name of the Student: ")
    python_marks = int(input("Python Marks: "))
    sql_marks = int(input("SQL Marks: "))
    ai_marks = int(input("AI Marks: "))
    total = python_marks+sql_marks+ai_marks
    avg = total/3
    
    Students.append({
        "id":sid,
        "sname":name,
        "stotal": total,
        "saverage" : avg,
        "sgrade": grade(avg),
        "sresult": result(avg)
    })

for s in Students:
    print(f"Student ID: {s['id']}")  
    print(f"Name of the Student: {s['sname']}") 
    print(f"Total of the Student: {s['stotal']:0f}") 
    print(f"Average of the Student: {s['saverage']:.2f}") 
    print(f"Grade of the student: {s['sgrade']}") 
    print(f"Result of the student: {s['sresult']}")
     
top = max(Students, key=lambda s:s["saverage"])
print(f"Highest Scoring Student: {top['sname']}")

high =[s["sname"] for s in Students if s["saverage"]>75]
print(f"Student Scoring above 75: {','.join(high)}")




