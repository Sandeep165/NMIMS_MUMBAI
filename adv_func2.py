'''
map(fun,iter1)   = 1
fun1 -> len
iter1 = [1]


filter(func,iter)   => 

wap take a list as a para and it will return a new lst of squar no
 (l1,l2) == newlst= []
'''




from operator import countOf
from posixpath import split


result = list(map(lambda a,b: a**b, [1,2,3,4,5],[2,6,5,4,7]))
print(result)

'''
input:---  
lst1 = [-1,-2,1,2,-5,5,-6,-66,1,2,3,10]

output:----
result =  [1,2,1,2,5,5,6,66,1,2,3,10]

'''
lst1 = [-1, -2, 1, 2, -5, 5, -6, -66, 1, 2, 3, 10]

result = list(map(abs, lst1))
print(result)


'''
var1 = 10
var2 = 10

1)importing re ......  (10+re)
2) 15 :- 
'''
country = ["mumbai","pune","delhi","goa","nashik"]
result =[["m","u","m","b","a","i"], ["g","o","a"]]

res = list(map(list,country))
print(res)

# var1 = list("hello")
# # ["hello"]
# print(var1)
'''
func(),iter1...map will apply that func to each and every data of thatr iterable
'''
ages = [10,15,41,18,20,16,19,33,31,11,14]
# age>18
ages = [10,15,41,18,20,16,19,33,31,11,14]

result = list(map(lambda x: True if x>18 else False,ages))
print(result)

'''



Q1:-  Write a Python program to convert all the characters 
in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function

Original Characters:
 {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

After converting above characters in upper and lower cases
and eliminating duplicate letters:
{('U', 'u'), ('O', 'o'), ('A', 'a'), ('B', 'b'), ('F', 'f'), ('I', 'i'), ('E', 'e')}

Q2:-  Write a Python program to create a new list taking specific
 elements from a tuple and convert a string value to integer.
 student_data  = 
 [('Alberto Franco','15/05/2002','35kg'), 
 ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), 
 ('Eesha Hinton','25/09/1998', '35kg')]

 Original data:
[('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), 
('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

Student name:
['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
Student dob:
['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
Student weight:
[35, 37, 39, 35]


Create a class with a few functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters with
 different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes.
 If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"

magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]

github desktop
'''

def names(a):
    return a[0]

def dob(b):
    return b[1]

def weight(c):
    return c[2][:-2]
    
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

stu_name = list(map(names, student_data))
print(stu_name)

stu_dob = list(map(dob, student_data))
print(stu_dob)

stu_weight = list(map(weight, student_data))
print(stu_weight)

s = {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

def upper_lower(a):
    return (a.upper(), a.lower())

result = set(map(upper_lower,s))


print(result)




