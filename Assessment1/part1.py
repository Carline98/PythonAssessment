#Find first largest number
mylist = [12,5,8,20,15]
largest_num = mylist[0]
for n in mylist:
  if n>largest_num:
    largest_num = n 
    print(largest_num)


#Character Frequency
value = "Programming"
count ={}
for x in value:
  if x in count:
    count[x]=count[x]+1
  else:
    count[x]=1
print(count)


#student mark analysis

Student = { "Carline" : 90 , "Prisilla" : 30 , "Johnson" : 23}
for name,marks in Student.items():
  if marks>40:
   print(name, ":" ,"PASS")
  else:
    print(name ,":" ,"FAIL" )
