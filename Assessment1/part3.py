#Text file
import csv
file = open("notes.txt","w")
file.write("hello1\n")
file.write("hello2\n")
file.write("hello3\n")
file.write("hello4\n")
file.write("hello5\n")

file = open("notes.txt","r")
content = file.read()
print(content)

file = open("notes.txt","r")
lines = file.readlines()
print(lines[3])


file = open("notes.txt","a")
file.write("carline")
file.close()


 #CSV file
with open("employees.csv", "w", newline = "") as file:
     writer=csv.writer(file)
     writer.writerow(["name","id", "salary"])
     writer.writerow(["car",123214,45000])
     writer.writerow(["carl",123214,75000])
     print("file created")






