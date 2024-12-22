# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

a=[1,2,3,4,5]
print(a[3:0:-1])
#-----------------------------------------------------------
arr=[[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop()) #pop removes last element from list
#---------------------------------------------------------------
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for  i in range(0,6):
    print(arr[i], end = " ")      
#---------------------------------------------------    



fruit_list1 =['Apple','Berry','Cherry','Papaya']
fruit_list2 =fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum=0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0] == 'Guava':
         sum += 1
    if ls[1] == 'Kiwi':
        sum+=20 
print(sum)            
#------------------------------------------------------------------------------------------
# TUPLE
# Tuple is exactly as similar as list datatype only the difference is that list is mutable but tuple is immutable that means we can not chnage the value

mytuple = ("prashant","ashish","rahul","sandip","komal","ankush","rajesh",23,3.15,77,"sandip")
print(mytuple)
print(type(mytuple))

lI=list(mytuple)
lI.append(2)
print(lI)
# --------------------------------------------------------------------------------------------=

# n=5
# sum=0
# my list=[]
# for i in range(N)
# a= in(input)        

#------------------------------------------------------------------------
import re
var= "gasgg54@#vscsd!s"
count=0
for i in var :
    z= re.findall('[a-z,0-9]q',i)
    z= ord(i)
    print(z)
    if z:
        if z>=97 and z<= 122:
            continue
    elif z>=48 and z<=57:
        continue    
    else:
        count+=1
print(count)        

#--------------------------------------------------------------------------

# indexing and slicing is not allowed in dictionary
# mydict ={
#     "name": "prashant"
#     "professional":"developer",
#     "empid":1001
#     }
# print(mydict)
# print(type(mydict))

#-----------------------------------------------------------------------------

mydict=  {
  101:"prashant",
  102:"ashish",
  "103":"mohini",
  "104":"trivani",
  101:"ashish",
  104:"ashish"
}
print(mydict)
a= mydict[102] #printed valued with the help of key
print(a)       #accesing value with key 102
#replacing the value with the help of key 
mydict[102]="peter"
print(mydict)
#printing key only key
for x in mydict:
    print(x)
for x in mydict.values():
    print(x)
#printing key and values both
for x,y in mydict.items():
    print(x,y)
# add new key 
mydict["mobile no"]=4646463738
print(mydict)        
#pop

my dict.pop(101)
print(mydict)






    


