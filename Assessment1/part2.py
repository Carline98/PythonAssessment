#Function
def calculate_bill(price,quantity):
    total = price * quantity
    if total >2000:
     total = total - (total *0.1)
    return total
print (calculate_bill(500,5))



#lambda_function
mylist =[12,5,18,7,24,9,30]
mul = list(map(lambda x:x*3, mylist))
print(mul)



#Recursion
def fact(n):
   if n==0 or n==1:
    return 1   
   return n * fact(n-1)
print(fact(5))



#String Processing
def count(text):
  vowels=0
  consonants=0
  space=0
  numbers = 0
  for char in text:
    if char.lower() in "aeiou":
      vowels = vowels+1
    elif char.isalpha():
       consonants =consonants+1
    elif char.isdigit():
       numbers= numbers+1
    elif char.isspace():
        space=space+1
  return vowels,consonants,numbers,space      

text ="Python 123"
v,c,s,n = count(text)    
print("vowel count" , v)
print("consonant count" ,c)
print("space count", s)
print("number count", n)





  


