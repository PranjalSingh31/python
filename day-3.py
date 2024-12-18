#list 
#string
#dictionary

#LIST

mylist = ["prashant","ashish","komal","ankush","ashish",77,"sandip",60.52,"prashant"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])     
print(mylist[1:8:2])           
             #mutable 
mylist[0]="akshay"
print(mylist)
#using list data type stack and queue is represented in python

mylist.append('harsh')  #append function is used to add the value at last position
mylist.append('laxman')
print(mylist)
 #insert function isused to add at a specific point or place

mylist.insert(2,"sanket")
print(mylist)

#remove fucntion is used to remove or delete data
mylist.remove("sandip")
print(mylist)

#cloning
newlist = mylist.copy()
print(newlist)

#2d list
mylist = [['prashant','jha'],['85.56'],[440022,"yyy"]]
print("example of multidimensional list:")
print(mylist)
#print(mylist[row][col])
print(mylist[0][0])  #prashant
print(mylist[0][1])  #jha
print(mylist[1][0])  #85.56
print(mylist[2][0])  #440022
print(mylist[2][1])  #yyy

#repeating code
# list1=["prashant","jha"]
# print(mylist1*2)

#list2 =[50,25.50]
#print(list1 + list2)

#del key word is used for deleting action 
#specific or particular value can be deleted

list2 = [50,25.50,'prashant']
del list2[2]
#for checking deletion print
# del list2
# print(list2)

#for emptying the list
list2= [50,25.50,'prashant']
list2.clear()
print(list2)

name="pranjal"
print(name)
myname=list(name)  #type casting
print(myname)

#reverse function
mylist = [40,30,20,10]
mylist.reverse()
print(mylist)

#SORTING
mylist =[44,22,77,0,9,88]
mylist.sort()
print(mylist)
#defaultsorting order for number is ascending order

#alising
#alising means assigning one variable reference to another
#variable
#mylist=[44,22,77,0,9,88]

mylist=[40,22,77,0,9,88]
for i in mylist:
    print(i)

container =[2,1,4,5,5,4,4,1,1]
count = 0
even = 0 
odd = 0
for i in container:
    if i==4:
        count = count+1
    elif i==2:
        even = even+1
    elif i==5:
        odd = odd+1
print(count-even)
print(count+odd)

data = [2,1,4,5,5,4,4,1,1]
max= min = data[0]
print(max)
print(min)
for i in range(len(data)):
    if data[i]>max:
        max = data[i]
    if data [i]< min:
        min = data [i]
# print('Max='max) 
# print('Min='min) 

mylist=[0,1,0,3,12]
N= len(mylist)
print(N)
for i in range(N):
    if mylist[2] ==0:
        mylist.remove(0)
        mylist.append(0)
print(mylist)        

mycart =[10,20,200,300,800,60,700]
for i in mycart:
    if i >400:
        print("This is my purchased cart item")
        continue
    print(i) 

#using else block
mycart = [10,20,800,60,70]
for item in mycart:
    if item > 400:    
        print("This is not in my budget")
        continue
    print(item)
else:
    print("you have purchased everything")

rollno = [3,5,7,1,11,4,5,2] 
for x in rollno:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print("which even no is found",x)
        break 

print('pranjal3891'.isalnum())
print('pranjalsingh'.isalpha())
print('311f'.isdigit())    
print('sdsdsdsd'.islower())

#max count of 1
mylist = [1,1,0,1,1,1,0,1,1,1,1]
consec_count =[]
count= 0
for i in mylist:
    if i ==1:
        count+=1
    else:
        consec_count.append(count)
        count = 0
else:
     consec_count.append(count)        
print(consec_count) 
#find th common

list1=[1,2,3,4]
list2=[3,4,5,6]
newlist=[]
for i in list1:
    if i in list2:
        newlist.append(i)
print(newlist) 

#classify the positive and negative numbers
mylist =[3,-2,7,-1,0,5,-4]
positive= 0
negative= 0
for i in mylist:
    if i>=0:
     positive +=1
    else:
        negative+=1
print(positive)
print(negative)        

#pattern
for i in range(1,4): #outerloop=row
    for j in range(1,4): #inner loop =col
        print(i,end='  ')
    print()

        
#   0 1 2 
# 0 1 1 1
# 1 2 2 2
# 2 3 3 3
# (i,j)=2,3

# n=int(input("enter the number if rows:"))
# for i in range (1,n+1):
#     for j in range (1,n+1)

n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end="  ")
    print() 

#palindrome

N= input ('Enter your string')
if N ==N [::-1]:
    print('palindrom')
else:
    print('Not palindrom') 

#ANAGRAM
s1= 'listen'
s2= 'silent'
list1 = list(s1)
list2 = list(s2)
print(list1)
print(list2)
list1.sort()
list2.sort()
if list1 == list2:
    print('Anagram')
else:
    print('not')

# PANGRAM

s="The quick brown fox jumps over the lazy dog"
flag=True
for i in range (1,27):
    if chr (64+i) not in s and chr (96+i) not in s:
        print ("not pangram")
        flag=False
        break
if flag == True:
    print("pangram")

#ASCII CODE is important 

name= "programmimg"
new_str=''
for i in name :
    if i not in new_str:
        new_str+=i
print(new_str)
     



