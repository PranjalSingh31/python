#Day 1 ( 16/12/2024)

math = 50
chemistry = 50 
phy =50

# used foe checking address
print(id (math))
print(id (chemistry))
print(id (phy))

#checking address

eng =40
hin = 40
print(id (eng))
print(id (hin))

math = 100
math = 49
print(id (math))

# swapping two num

num1 = 20
num2 = 40 

temp = num1
num1= num2 
num2 =temp 

print(num1)
[print(num2)]

#swapping of two nums without using third variable 

a = 100
b = 200

a= a+b  #a=100+200
b=a-b
a=a-b

print(a)
print(b)

#claculate three papers marks 

p1= 2
p2 = 10 
p3 = 15 
percentage = (p1+p2+p3)/3

#Type casting 

print(2+2)
print( '2'+'3')
# a= input('enter first value')
# b= input('enter second value')
print(a+b)

#int ()used to convert in integer 3.24=int=3
print (int (3.14 ))
#print (int(10+5j))
print(int (True))#=1
print(int(False))#=0
#print (int("4.22"))
print(int("4"))

#flaot() used to convert
print(float(True))
#print(float(50+2j))
print(float (True))
print(float (False))
print(float (4.22))
print(float ("4"))
#print(float("name"))
#we cannot convert complex value to float 

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
# print (complex("name"))

print(complex(5,-3))
print(complex(True, False ))

#boolean 
# True =1
#False =0
#################

x=10 
y=20 
print (x is y ) #false 

# membership operstor is used to check that object is present or not in collection data structure
# returns true and false 
a="pranjal singh"
print('pra'in a) # true 

##################################################################################################################################

#string slicing

name="pranjalsingh"
 #01234567891011
name [0:5] #pranj
name [1:]  #ranjalsingh
name[:] #pranjalsingh
name[1:8:2] #rjs
#prints the  required characters
#reverse the string 
name[::-1]

# find function 

s= "python is object oriented programming language "
print(s.find("python"))
print(s.find("java"))
print(s.find("programming"))


s="pranjal","atharv","ayush"
m='$'.join(s)
print(m)

#.lower
#.upper
#.swapcase
#.title
#.capitalize

s="python are HIGH LEVEL PROGRAMMING LANGUAGE "
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

name="pranjal"
sal= 5000
age= 20
# print("{}sal is {}age is{}".fomat(name,sal,age))
# print("{}name is {}age is{}".fomat(name,sal,age))

#####################################################################################################################
# simple if 
 
ch= int(input('Enter any number'))
if ch>0:
    print('Positive')

if ch == 0:
    print('Negative')    

if ch== 0:
    print('Zero')    

# num1 = int(input ('enter any number')) 
# num2 = int(input ('enter any number')) 
# num3 = int(input ('enter any number')) 
# num4 = int(input ('enter any number')) 
# num5 = int(input ('enter any number')) 

# if num1 > num2 and num1 >num3 and num4 >num1 and num5 >num1:
#     print(num1,'is greater')
# if num2 > num1 and num2 >num3 and num2 >num1 and num5 >num2:
#     print (num2 ,'is greater ')
# if num3 > num2 and num3 >num1 and num4 >num3 and num5 >num3:
#     print(num3,'is greater')
# if num4 > num2 and num4 >num1 and num4 >num3 and num5 >num4:
#     print(num4,'is greater')
#  if num5 > num2 and num5 >num1 and num5 >num3 and num5 >num3:
#     print(num5,'is greater')
 
#wap to check weekend
 
# day= input("Enter Day")
# if day == "saturday" or day =="sunday "or day== 'saturday' or 'SATURDAY'
#      print("WEEKEND")
#      else:
#         print("WORKING DAY ")


#elif can be used in place of else if 

# ch= ord(input("Enter any character"))
# #ord function used to covert in ASCII code
# if  ch >= 65 and ch <=91:
#     print("your entered character is in upper case") 
# elif ch>=97 and ch<122:
#     print("your entered character is in lower case") 
# elif ch>=48 and ch<=57:
#     print("your entered character is in digit") 
# else:
#     print("your entered character is special symbol")
         
###########
# for loop 
#for(initialization;condition;inc/dec)
for i in range(1,10,2): #i=1 #running on gap of 2 till 10 
    print(i)

for i in range(1,11): #i=1 
    print(i*2,'',i*3,'',i*4) 
    print()

for i in range(1,11):
    print(i*11,'',i*12,'',i*13)

a='shiwaleew'
  #012345678
for i in a: #i=9:w
    if i=='w':
        print(i)




name='prashantjha'
count_consonent=0
count_vowel=0

for i in name: 
    if i== "a"or i== "e"or i== "i" or i== "o" or i=="u" :
        count_vowel=count_vowel+1
else:
    count_consonent+=1
print('count consonent=',count_consonent)
print('count vowel=', count_vowel)

for i,j in zip(range(1,6),range(5,0,-1) ):  # multiple range function can be taken in zip function
    if i==3 and j==3:
         continue
    print (i,'',j) 

p1=int(input("Enter paper1 marks"))  #45
p2=int(input("Enter paper2 marks"))  #55
p3=int(input("Enter paper3 marks"))  #77
p4=int(input("Enter paper4 marks"))  #88
p5=int(input("Enter paper5 marks"))  #65

gender= input('Enter your gender')
if p1 >=40 and p2>=40 and p3>=40 and p4>=40 and p5>=40:
        print("you are pass")
else:
    print("you are fail")
total = p1+p2+p3+p4+p5
percentage = total/5.0
print ("Total=",total)        
print("percentage=",percentage)

if(gender == 'male'and percentage>=60):
    print("selected")
if(gender == 'female'and percentage>=65):
    print("selected")
else:
    print("Not selected")
    