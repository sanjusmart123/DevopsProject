'''
1.Basics of Python
2.	Control Flow
3.	Functions and Scope
4.	Data Structures
5.	Classes and Objects (OOP)
6.	Modules and Packages
7.	Error Handling and Exceptions
8.	File Handling
9.	Iterators and Generators
10.	Comprehensions
11.	Decorators and Closures
12.	Regular Expressions
13.	Multithreading and Multiprocessing
14.	Networking
15.	Database Interaction
16.	Data Science and Visualization (Popular Libraries)
17.	Web Development
18.	Testing and Debugging
19.	Version Control with Git
20.	Advanced Topics
21.	Python Tools and Best Practices
'''

#1.	Basics of Python
#svariable
Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
x = 5
y = "sai"
print(x)
print(y)
Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x) #Orange
print(y) #Banana
print(z)#Cherry

The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)#Python is awesome
###############################################
The best way to output multiple variables in the print() function 
is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)
##############################
#sglobal Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

a="sai"
def greet():
    print(f"good morning {a}")
greet()

when we create a same variable inside the function it takes inside the variable not outside the variable.
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
def greet():
    global a
    a="sanju"
    print(f"good morning {a}")
greet()

Also, use the global keyword if you want to change a global variable inside a function.
a="sai"
def greet():
    global a
    a="sanju"
    print(f"good morning {a}")
greet()

#################################
#slocalvariable
A local variable is a variable declared inside a function, and its scope is limited to that function. 
It is created when the function is called and destroyed when the function terminates.
 = 20  # Global variable

def example():
    x = 10  # Local variable
    print(f"x inside the function: {x}")

example()
print(f"x outside the function: {x}")  # Global variable remains unchanged

##############################
#casting
Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
x = str(4)    # x will be '5'
y = int(5)    # y will be 5
z = float(3)  # z will be 3.0
################################
You can get the data type of a variable with the type() function.
x = 5
y = "sai"
print(type(x)) #integer
print(type(y)) #string
#################################
Case-Sensitive
Variable names are case-sensitive.
This will create two variables:
a = 4
A = "Gulivindala"
###############################
#text type
#string data type
single line strings are form with single or double quotes
a='sai'
Multiline Strings
You can assign a multiline string to a variable by using three quotes:
a='''sai,gulivindala,python,java'''
print(a)

x=str("sai")
print(x)       
print(type(x))

#concatenation
a="sai"
b="Gulivindala"
c=a+b
d=a+" "+b
print(d)#sai Gulivindala
##########################################
To specify a string as an f-string, simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.
name="sai"
print(f"my name is {name}")
#############################################
Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
txt=f"price is {10 * 10}rs"
print(txt)
##############################################
price=20
txt=f"The Book price is {price:.2f} dollars"
print(txt) #The Book price is 20.00 dollars
############################################
The escape character allows you to use double quotes when you normally would not be allowed:
a="python is a \"programming\" language"
print(a)  #python is a "programming" language
################################################
#sstringmethods
a='python is a "programming" language'
print(a.capitalize())   #convert first character uppercase

a='python is a "programming" language'
print(a.count("i")) #Returns the number of times a specified value occurs in a string

a='python is a "programming" language'
print(a.find("r")) #return position of r

a='python is a "programm1ing" language'
print(a.isalnum()) #False

a="saigulivindala"
print(a.isalpha()) #True

a="sai gulivindala"
print(a.isalpha()) #False

a="abc123"
print(a.isalnum()) #True

a="123"
print(a.isdigit()) #True

a="my name is sai gulivindala"
print(a.title()) 


#############################################
#sslicing
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

a='Sai, gulivindala '
print(a[1:7])#
print(a[:7])
print(a[::-1])#reverse
print(a[-1:]) #a
print(a[:-1])#sai gulivindal
print(a[:])#total string
print(a[:-2])#last 2 remove
print(a[:-15])#empty
print(a[-2:])#la
print(a[-15:])#sai gulivindala

print(a.upper())
print(a.lower())
print(a.strip())#remove whitespaces 
print(a.replace("g","G"))

#The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))#['Sai', ' gulivindala ']

#remove the whitespace inside the string
result=a.strip().replace(" ","")
print(result)
####################################################

#############################################
#These 3 types are numeric type
#integer,float,complex data types 
x=int(20)
print(x)      
print(type(x))

x=float(12.0)
print(x)             
print(type(x))

x=complex(1j)
print(x)
print(type(x))
#we can convert int to float datatype or viceversa and complext data type
###############################################
#sequence type
#list,tuple,range
my_list=[1,2,2.3,1+2j,{"name": "sai"},{1}]
my_list2=list((1,2,2.3,1+2j,{"name": "sai"}))
print(my_list)
print(my_list2)

my_tuple=(1,3,2.4,1+2j,{"name": "guli"},{3})
my_tuple2=tuple((1,4,2.3,1+2j,{"name": "python"}))
print(my_tuple)
print(my_tuple2)         

x=range(10)
print(x)
print(type(x))
#######################################################
#set type
#set and frozenset
my_set = {1,2,3,1+4j,2.5,2}
print(type(my_set))
my_set2 = set((1,2,3,1+4j,2.5,2,(2,4)))
print(my_set2)

my_frozenset=frozenset({1,2,3,1+4j,2.5,2,(2,4)})
print(my_frozenset)
print(type(my_frozenset))
###################################################
#boolean type
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
####################
print(1 < 10) #T
print(10 == 5)#F
print(4 > 2)#T
print(10 != 6)#T
print(5 <= 5)#T
print(7 >= 5)#T
####################
a=10
b=20

if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
#################################
print(bool(123))   # Output: True
print(bool("sai")) # Output: True
print(bool())      # Output: False

bool(123): Any non-zero number is considered True in Python.
bool("sai"): Any non-empty string is considered True in Python.
bool(): Without any argument, the bool() function returns False.


bool(False)
bool(None)
bool(0)
bool("")      #All are False
bool(())
bool([])
bool({})
##########################################
def myFun():
    return False
if myFun():
    print("YES")
else:
    print("NO")

######################################################
#stypeconversion
Type Conversion
we can convert from one type to another with the int(), float(), and complex() methods:

x=12
y=2.5
z=1+3j

a=float(x)
b=int(2.5)
c=complex(y)
#d=int(z) #we canot convert complex to int
e=str(y) #12
print(a)
print(b)
print(c)
#print(d)
print(e)
print(type(e))
import random

print(random.randrange(1,10))



######################################
#srandomnumber
Random Number
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1,10))



###############################
#soperators
#sarthemeticoperators
+,-,*,/,//,%,**
x=5
y=3

print(x+y)#8
print(x-y)#2
print(x*y)#15
print(x/y)#1.6666
print(x//y)#1
print(x%y)#2
print(x**y)#125
#####################
#sassignmentoperators
x=10

x += 10
print(x)  #20

x -= 5
print(x) #15

x *= 5
print(x)  #75

x //= 5
print(x) #15

x /= 5
print(x)  #3.0

x %= 5
print(x)   #x = x%5

x **= 5
print(x)  #power

print(a := 7)
 x=7
 print(x)
##############################
#comparisionopearators
==
5==5 True

!=
5!=4 True

>
5 > 7 False

<
5 < 9 True

>=
5 >= 5 True

<=
5 <= 3 False

#logicaloperators

and   #returns True if both expressions true
5 > 2 and 4 < 7

or   #returns True if one is True
10 < 20 or 10 > 20

not  #reverse the result
not(7 < 10)  False

#bitwiseoperators
&(AND), `,^(XOR),~(Not),<<(left shift),>>(right shift)

#identityopearators
is       #if both objects same name
x=[1,2,3]
y=[1,2,4]
print(x is y)#False


is not   #True if objects are not same  
x=[1,2,3]
y=[1,2,4]
print(x is not y)#False

x=[1,2,3]
y=[1,2,4]
print(x == y) #True
#here it checks data inside the variable 
#membershipopearator
in     #used to check items in sequences like lists,tuples,strings
x=[1,2,3]
print(2 in x)
print(7 in x)

not in    #returns True if value does not exist
print("a" not in "sai") #False
print("k" not in "sai")#True

#ternaryoperator
age=18
status="adult" if age >= 18 else "minor"
print(status)
###########################################################
#slists

my_list=[True,False,True]
my_list2=list((1,2,"sai",{3},{"name":"python"}))
print(my_list2)

print(my_list2[-1:]) #[{'name': 'python'}]
print(my_list2[-1])  #{'name': 'python'}
print(my_list2[:-1])  #[1, 2, 'sai', {3}]
print(my_list2[-5:])  #[1, 2, 'sai', {3}, {'name': 'python'}]
# print(my_list2[:-5])  #[]

if "sai" in my_list2:
    print("sai is exist")
else:
    print("not exist item")
#updating value   
my_list[2]=False
print(my_list)

my_list[0:2]= [False,True]
print(my_list)

my_list[0:2]= [False]
print(my_list)

my_list2.insert(2, "gulivindala")
print(my_list2)

my_list.extend(my_list2)
print(my_list)

my_list2.extend([3,5])
print(my_list2)

my_tuple=(1,2,3,4)
my_list2.extend(my_tuple)
print(my_list2)

my_list.pop(2)
print(my_list)

del my_list2[3]
print(my_list2)

#del my_list2
#print(my_list2)

my_list.clear()
print(my_list)

for i in range(len(my_list2)):
    print(my_list2[i])
######################################
my_list5=["sai","Python","java"]
i=0
while i < len(my_list5):
    print(my_list5[i])
    i += 1
###########################################
my_list5=["sai","Python","java"]
[print(i) for i in my_list5]
######################################
my_list=["sai","python","java"]
sai_list=[]
for i in my_list:
    if "a" in i:
     sai_list.append(i)
print(sai_list)
######################################
my_list=["sai","python","java"]
sai_list=[x for x in my_list if "a" in x]
print(sai_list)
######################################
#set all values to new_list to "sai"
my_list=["python","Java","Devops"]
new_list=["sai" for x in my_list]
print(new_list)
########################################
#replace JAva with C++
my_list=["python","Java","Devops"]
new_list=[x if x != "Java" else "C++" for x in my_list]
print(new_list)
#########################################

my_list = [1,2.5,"sai",True,1+3j,6]
my_list.append(4)
my_list.insert(2,5)
my_list.extend([6,7,8])
my_list.remove(2.5)
item=my_list.pop(2)
print(item)
del my_list[3]
#del my_list
#my_list.clear()		
print(my_list)
#####################
#indexing
print(my_list[2])
print(my_list[1:2])
print(my_list[:2])
print(my_list[::-1])
#my_list.sort()
print(my_list)

new_list=sorted(my_list)
print(new_list)
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.index(6))
print(my_list.count(6))

sai_list = my_list.copy()
print(sai_list)
####################
#modification
sai_list[1] = 13
print(sai_list)
####################
#checking nd len
print(len(sai_list))
print(2 in sai_list)
print(8 in sai_list)
#######################
#list comprehensions
squared_list = [x **2 for x in sai_list]
print(squared_list)
even_numbers=[x for x in sai_list if x%2 == 0]
print(even_numbers)
######################
#nested list
nest_list=[[1,2],[3,4],[5,6]]
print(nest_list[1])
print(nest_list[1][0])
###############################
#stuple
'''
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.'''
my_tuple=(1,2,3,4)
#sindexing
print(my_tuple[3]) #4
print(my_tuple[1:3])
print(my_tuple[::-1])
print(my_tuple[-1])
print(my_tuple[-1:-3])
#################################
#we know tuple is immutable ,if we need to update the tuple first tuple convert to list 
#and update or remove or add items and again convert to tuple
my_tuple=("python","Devops")
my_list=list(my_tuple)
my_list[1]="SQL"
print(my_list) #['python', 'SQL']
#################################
#unpacking tuple
my_tuple=("python","Devops")
(OOPS,Jenkins) = my_tuple
print(OOPS)
##################################
#Add Asterisk* tuple
my_tuple=("python","Devops","AWS")
(OOPS,*Jenkins) = my_tuple
print(OOPS)    #python
print(Jenkins) #['Devops', 'AWS']
####################################
#for loop
my_tuple=("python","Devops","AWS")
for i in range(len(my_tuple)):
    print(my_tuple[i])
#####################################
#while loops
my_tuple=("python","Devops","AWS")
i=0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1
###################################

#sconcate
your_tuple=(5,6,7,8)
both_tuple=my_tuple+your_tuple
print(both_tuple)

repeated_tuple= my_tuple *3
print(repeated_tuple)

#checking
print(4 in my_tuple)
print(2 not in my_tuple)

#len
print(len(my_tuple))
print(my_tuple.count(2))
print(my_tuple.index(3))
#unpacking
a,b,c,d= my_tuple
print(a,b,c,d)
######################################
#type
my_tuple=("python",)
print(type(my_tuple))  #<class 'tuple'>

my_tuple=("python")
print(type(my_tuple))  #<class 'str'>

#####################################
#ssets
'''Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.'''
#################################
my_set={2,3,True,1} #{True, 2, 3}
print(my_set)#TRue and 1 considered as same value 

my_set2={2,3,0,False} #{0, 2, 3}
print(my_set)#False and 0 considered as same value

for i in my_set:
    print(i)   
    
print(3 in my_set) #True

my_set.add(6)
print(my_set)   #{True, 2, 3, 6}

my_set.update(my_set2)
print(my_set) #{0, True, 2, 3, 6}
  
#####################################
my_set = {1,2,3,4,4}
print(my_set)
my_set2=set()
my_set3=set([1,2,3,4,4])
print(my_set3)
my_set4={"A","B","C"}
my_set.add(5)
print(my_set)
my_set.update([6,7],(8,9,8))
print(my_set)
my_set.remove(7)
print(my_set)
my_set.discard(0)
print(my_set)
my_set.pop()
print(my_set)
#my_set.clear()
print(my_set)

my_set4.pop()
print(my_set4) #randing item pop

union_sets=my_set | my_set4 #Both combine sets
print(union_sets)

Both_sets = my_set.union(my_set4)
print(Both_sets)

add_two_sets=my_set.update(my_set4)
print(add_two_sets)

my_set={0,1,4,5,6}
my_set2={0,7,9,4}
my_set3={"sai","gulivindala"}

my_set4=my_set.union(my_set2,my_set3)
print(my_set4)

my_set={0,1,4,5,6}
my_set2={0,7,9,4}
my_set3={"sai","gulivindala"}

my_set4=my_set | my_set2 | my_set3
print(my_set4)

'''Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.'''

my_set={1,2,3}
my_tuple=(1,2,3,4)

Both_set_tuple=my_set.union(my_tuple)
print(Both_set_tuple)   #{1, 2, 3, 4}




intersection_sets=my_set & my_set3 #common items in both sets 
print(intersection_sets)

Both_sets=my_set.intersection(my_set3)
print(Both_sets)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
difference_sets=my_set - my_set3  #sets contain elements first set not in but not in second set
print(difference_sets)

Both_sets=my_set.difference(my_set3)
print(Both_sets)

#Symmetric Differences
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
symmetric_diffrence_sets = my_set ^ my_set3 #avoid common items and print remaining items in both sets
print(symmetric_diffrence_sets)

Both_sets = my_set.symmetric_difference(my_set3)
print(Both_sets)

print(len(my_set))
####################################
#sfrozenset

my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # Error: 'frozenset' object has no attribute 'add'
# my_frozenset.remove(2)  # Error: 'frozenset' object has no attribute 'remove'

# Frozensets can be used as dictionary keys

my_frozenset=frozenset({1,2,3,1+4j,2.5,2,(2,4)})
print(my_frozenset)
print(type(my_frozenset))

'''output
frozenset({1, 2.5, 3, 2, (2, 4), (1+4j)})
<class 'frozenset'>
'''

'''Use set when:

we need a mutable collection of unique elements.
The set will undergo frequent updates (add/remove operations).

Use frozenset when:
we need an immutable collection of unique elements.
The set is used as a key in a dictionary or an element in another set.'''

####################################
#sdictionary
#Dictionary
"""Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries cannot have two items with the same key"""

my_dict = {"name": "sai","age":24}
print(my_dict)

x=my_dict.items()
print(x) #dict_items([('name', 'sai'), ('age', 24)])

my_dict2 = dict(name = "Python",version = 3.10)
print(my_dict2)

my_dict2=dict({"name":"python","version":3.12})
print(my_dict6)

my_dict["phno"] = 9392751509

my_dict.update({"gmail": "saig@","Pass": 9392751509})
print(my_dict)

my_dict2["usrname"] = "saigulivindala"
print(my_dict2)

my_dict2.update({"datatype": "list","datatype2": "tuple"})
print(my_dict2)

#new_removed = my_dict.pop("age")
#print(new_removed)

my_dict={"name":"sai","age":25}
my_dict.pop("name")
print(my_dict)

my_dict21=(1,2,3,4,5,4)
ram=my_dict21[3]

print(ram)

sai=my_dict["name"]
print(sai)

del my_dict["name"]
print(my_dict)

#del my_dict
removed_item = my_dict.pop("age")
print(removed_item)

pop_item = my_dict.popitem() #removes last item
print(my_dict)

#my_dict.clear()
print(my_dict)

print("name" in my_dict)
print("phno" in my_dict)

print("saig@" in my_dict.values())
print(my_dict)

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)
    
for key,value in my_dict.items():
    print(key,":",value)
    
sai_dict = my_dict.copy()
print(sai_dict)
print(my_dict)

my_dict={"name":"Python","version":3.12}
copy_dict=dict(my_dict)
print(copy_dict)
############################
my_family={"Father":{ "Name": "Ramakrishna","age": 50}, "Mother":{"Name":"Yerakamma","age": 35}}
print(my_family)
print(my_family["Father"]["Name"])

for x, obj in my_family.items():
    print(x,obj)
    for y in obj:
        print(y+ ":",obj[y])
    
'''{'Father': {'Name': 'Ramakrishna', 'age': 50}, 'Mother': {'Name': 'Yerakamma', 'age': 35}}
Ramakrishna
Father {'Name': 'Ramakrishna', 'age': 50}
Name: Ramakrishna
age: 50
Mother {'Name': 'Yerakamma', 'age': 35}
Name: Yerakamma
age: 35'''
##################
import copy
nested_dict = {"language": {"name":"java","version": 3.15}}
g_dict = copy.deepcopy(nested_dict)
print(g_dict)
print(len(my_dict))

########################################################
#scontrolflowstatements
#sif elif else :
lastball = 4
if lastball >= 6:
    print("Won the match")
elif lastball == 5:
    print("Draw match")
else:
    print("Lost the match")
###################################
a=100
b=50
c=200
if a < b and b < c:
    print("True")
else:
    print("False") #False
    
if a < b or b < c:
    print("True")
else:
    print("False") #True
    
if not a < b and b < c:
    print("True")
else:
    print("False")# True, it is opposite of first expression
###################################################################
#snestedif
x=int(input()) #15

if x > 20:
    print("above twenty")
    if x > 50:
        print("also above 50")
    else:
        print("but not above 50")
else:
    print("below 20") #below 20
#####################################################

branch_name=input()
build_status =input()
if branch_name == "develop":
    if build_status == "success":
        print("deploying to staging env")
    else:
        print("build failed,Not deploying to staging")
elif branch_name == "master":
    if build_status == "success":
        print("deploying to production env")
    else:
        print("build failed,Not deploying to production")
        
else:
    print("deploying to feature branch,no deployment triggered")
######################################################################  
#sternoryoperator or conditional expressions
a=100
b=200
print("a is greater than b") if a > b else print("b is greater than a")

a=100
b=100
print("a is greater than b") if a > b else print("a is equal to b") if a==b else print("b is greater than a")

###############################################################
import os
print("File exists") if os.path.exists("/home/usr/sai.txt") else print("File does not exist")
#Checks if the file exists at the specified path.

import os
for file_path in ["/home/usr/devops.txt","/home/usr/aws.txt","/home/usr/kubenernetes.txt"]: print(f"{file_path} exists" if os.path.exists(file_path) else f"{file_path} does not exists")

import os
print("all files exists") if all(os.path.exists(file) for file in ["/home/usr/pyhton.txt","/home/usr/devops.txt","/home/usr/aws.txt"]) else print("some files missing")

#sternary operator if elif else
server_status = int(input())
status = "up" if server_status ==1 else "down" if server_status ==0 else "unknown"
print(status)

if server_status == 1:
    status = "up"
elif server_status == 0:
    status = "down"
else:
    status = "unknown"

print(status)
########################################################################
#sfor loop
'''For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

sai=110
for sa in range(100):
    if sai >= 70 and sai <= 100:
        print("not ok")
        break
        
    elif sai <70:
        print("its ok")
        break
    else:
        print("exceeded")
        break
##############################################################
x=["sai","saigulivindala","Phno"]
for i in x:
    print(i)
    if i == "saigulivindala":
        break 
#######################################
x=["sai","saigulivindala","Phno"]
for i in x:
    if i == "saigulivindala":
        continue
    print(i)

        
##############################################################        
n=10
for i in range(n):
    if i <= 25:
        print("low marks")
        
    elif i <=50:
        print(" avg marks")
        break
    elif i <= 75:
        print("good")
        
    else:
        print("exellent")
##################################
#sfor
tasks = ["build", "test", "deploy"]

for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}")
##################################
#snestedfor        
environments = ["development","staging","production"]
servers =["web1","web2","web3"]
for server in servers:
    for env in environments:
        print(f"checking health of {server} in {env} environment")
        
####################################################
#swhile_loop

'''while Loop
With the while loop we can execute a set of statements as long as a condition is true.'''
###################################
'''continue Statement
With the continue statement we can stop the current iteration, and continue with the next:'''
i=0
while i < 10:
    i +=1
    if i == 7:
        continue
    print(i)
    
#it will skip the 7 and continue with the next iteration
##################################
'''break Statement
With the break statement we can stop the loop even if the while condition is true:'''

i=1
while i < 10:
    print(i)
    if i == 7:
        break
    i +=1
#it will stop with 7 
##################################
#With the else statement we can run a block of code once when the condition no longer is true:
i=1
while i < 10:
    print(i)
    i +=1
else:
    print("i is no longer less than 6")
    
#Here print the both statements
##################################
import time
cpu_usage = 76
while cpu_usage < 90: print("High alert!" if cpu_usage > 80 else "normal usage"); time.sleep(3)
#########################################
import time

cpu_usage = int(input())  
while cpu_usage < 90:
    if cpu_usage > 80:
        print("High alert!")
        break
    else:
        print("normal usage")
        time.sleep(3)
    cpu_usage += 2     
        


########################################
#3.	Functions and Scope
#sfunctions

'''In Python, functions are blocks of reusable code that perform a specific task. 
They help in organizing code, making it more readable, modular, and maintainable. 
Functions allow us to write once and use the same code multiple times by calling the function.'''

'''Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.'''
def greet(name):
    message = f"Good Morning, {name}"
    return message

print(greet("sai"))
print(greet("sai gulivindala"))
##########################################
import math
print(dir(math))
help(math)
##########################################
import inspect
import module_name

print(inspect.getmembers(module_name))
##########################################
import requests

def trigger_jenkins_job(job_name, jenkins_url, token):
    url = f"{jenkins_url}/job/{job_name}/build?token={token}"
    response = requests.post(url)
    if response.status_code == 201:
        print("Jenkins job triggered successfully.")  
    else:
        print(f"Failed to trigger job: {response.status_code}")

trigger_jenkins_job("my-job", "http://jenkins.example.com", "my-token")
'''1.jenkins_url: The base URL of the Jenkins server (e.g., http://jenkins.example.com).
2.token: A token used for authentication to trigger the job. 
This is typically generated within Jenkins for security.
3.Jenkins' REST API provides a way to trigger jobs via the /build endpoint
4.requests.post(): Sends a POST request to the URL to trigger the Jenkins job.
requests is a popular Python library for making HTTP requests.'''
###########################################
def create_terraform_tfvars(instance_data):
    
    tfvars_content = ""
    for data in instance_data:
        tfvars_content += f"""
instance_type = "{data['instance_type']}"
ami_id        = "{data['ami_id']}"
"""
    
    
    with open("terraform.tfvars", "w") as file:
        file.write(tfvars_content)


instance_data = [
    {"instance_type": "t2.micro", "ami_id": "ami-123385646"},
    {"instance_type": "t2.small", "ami_id": "ami-3648026249"},
    {"instance_type": "t2.medium", "ami_id": "ami-845232103"}
]


create_terraform_tfvars(instance_data)

'''1.tfvars_content = "":

Initializes an empty string called tfvars_content.
This string will accumulate the Terraform variable definitions for each instance in the instance_data list.
2.for data in instance_data::

Starts a loop that iterates over each item in instance_data.
data represents one dictionary from the list, which contains keys like instance_type and ami_id.

3.Formatted String (f"""):
Creates a multi-line string using an f-string, which allows the insertion of values directly into the string using placeholders ({}).
4.Appending to tfvars_content:
Each iteration appends a new block of text to tfvars_content.
{data['instance_type']}:
5.Replaces {data['instance_type']} with the value of the instance_type key from the data dictionary.
{data['ami_id']}:
Replaces {data['ami_id']} with the value of the ami_id key from the data dictionary

6. with open("terraform.tfvars", "w") as file:
open():
Opens or creates the file terraform.tfvars.
The first argument, "terraform.tfvars", is the name of the file you want to open.
"w" mode:
The second argument "w" stands for write mode. This means:
If the file already exists, it will be overwritten (its previous content will be erased).
If the file doesn't exist, it will be created.
with statement:
Ensures automatic resource management.
The file is automatically closed once the block of code under with is done, even if an error occurs.
 This prevents issues like leaving a file open accidentally, which could lead to resource leaks or file corruption.'''
##############################################
#sarbitary_arguments
'''Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:'''

def my_function(*names):
    for name in names:
        print(f"Hello {name}")
my_function("sai","sanju","virat","dhoni")

'''Hello sai
Hello sanju
Hello virat
Hello dhoni'''

def deploy_apps(*apps):
    for app in apps:
        print(f"Deploying application: {app}...")
        
        print(f"Application {app} deployed successfully ")

deploy_apps("web-app", "api-server", "worker")
##########################################
#skeywordarguments
'''Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.'''

def deploy_pod(namespace, image,pod_name):
    print(f"Deploying pod '{pod_name}' in namespace '{namespace}' using image '{image}'.")
    
deploy_pod(pod_name="my-app", namespace="dev", image="nginx:latest")
##############################################
#sarbitarykeywordarguments
'''Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.'''
def configure_container(**config):
    print(f"Container configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

configure_container(image="nginx:latest", port="8080", env="production", name="web-server")
##########################################
def my_fun(food):
    for i in food:
        print(i)
fruits=["apple","Banana","cherry"]
my_fun(fruits)
##########################################
#spositional-Only Arguments
'''You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
To specify that a function can have only positional arguments, add , / after the arguments:'''
def my_fun(x, /):
    print(x)
my_fun(5)
##########################################
#skeywordonly arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)
##########################################
#recursion
'''A Function calls itself is known as Recursive function and its technic is know as Recursion.
These should be at least one if statement used to terminate recursion.
It doesnot contain any looping statements'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1) #here call its self till condition is satishfy
print(fact(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6)) #8 6th fibonacci series is 8  0,1,1,2,3,5,8

##########################################
#sfunctionsinsidenestedfor
import requests

def scrape_prometheus_metrics(exporters, environments):
    for exporter in exporters:
        for env in environments:
            
            url = f"http://{exporter}-{env}.example.com:9090/metrics"
            print(f"Scraping metrics from Prometheus exporter: {url}...")
            
            response = requests.get(url)
            
            if response.status_code == 200:
                print(f"Metrics successfully scraped from {url}.")
            else:
                print(f"Failed to scrape metrics from {url}, Status code: {response.status_code}")

scrape_prometheus_metrics(
    ["api-exporter", "web-exporter"], 
    ["staging", "production"]
)
'''Scraping metrics from Prometheus exporter: http://api-exporter-staging.example.com:9090/metrics...
Failed to scrape metrics from http://api-exporter-staging.example.com:9090/metrics, Status code: 404

Scraping metrics from Prometheus exporter: http://api-exporter-production.example.com:9090/metrics...
Metrics successfully scraped from http://api-exporter-production.example.com:9090/metrics.

Scraping metrics from Prometheus exporter: http://web-exporter-staging.example.com:9090/metrics...
Failed to scrape metrics from http://web-exporter-staging.example.com:9090/metrics, Status code: 500

Scraping metrics from Prometheus exporter: http://web-exporter-production.example.com:9090/metrics...
Metrics successfully scraped from http://web-exporter-production.example.com:9090/metrics.'''

###############################################
#sfunction_inside_nestedif_and _nestedfor
def check_pod_health(namespaces, pods_status):
    for namespace in namespaces:
        print(f"\nChecking pods in namespace: {namespace}...")
        for pod, status in pods_status[namespace].items():
            if status.get("running"):  
                if status.get("ready"):  
                    print(f"Pod {pod} is running and ready.")
                else:
                    print(f"Pod {pod} is running but not ready.")
            else:
                print(f"Pod {pod} is not running.")


pods_status = {
    "namespace1": {
        "pod1": {"running": True, "ready": True},
        "pod2": {"running": True, "ready": False},
        "pod3": {"running": False, "ready": False}
    },
    "namespace2": {
        "pod4": {"running": True, "ready": True},
        "pod5": {"running": False, "ready": False}
    }
}


namespaces = ["namespace1", "namespace2"]

check_pod_health(namespaces, pods_status)

'''Checking pods in namespace: namespace1...
Pod pod1 is running and ready.
Pod pod2 is running but not ready.
Pod pod3 is not running.

Checking pods in namespace: namespace2...
Pod pod4 is running and ready.
Pod pod5 is not running.'''

###############################################
#sfunctioninsidewhile
import requests
import time

def send_health_alert(app_name):
    print(f"ALERT: {app_name} is down!")

def monitor_app_health(app_name, health_url, poll_interval=10):
    while True:
        
        response = requests.get(health_url)
        
        if response.status_code == 200:
            print(f"{app_name} is healthy.")
        else:
            send_health_alert(app_name)
            break
        
        time.sleep(poll_interval)


monitor_app_health("MyApp", "http://myapp.example.com/health", poll_interval=5)
'''MyApp is healthy.
MyApp is healthy.
ALERT: MyApp is down!
'''
################################################
#sternaryoperatorfunction
import boto3; boto3.client('s3').upload_file('local_file.txt', 'my-bucket', 's3_file.txt')
########################################################
#slambdafunction
Python Lambda
'''A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression'''

x=lambda a,b:a*b
print(x(3,5))
#########################################
def my_fun(n):
    return lambda a: a*n
my_lambda_arg=my_fun(5) #this is lambda argument
print(my_lambda_arg(10))
#########################################
import boto3
list_s3_buckets = lambda: [print(bucket['Name']) for bucket in boto3.client('s3').list_buckets()['Buckets']]
list_s3_buckets()
###########################################################################################################
import boto3
list_iam_users = lambda: [print(user['UserName']) for user in boto3.client('iam').list_users()['Users']]
list_iam_users()
################################################
#spythonarrays
#Python does not have built-in support for Arrays, but Python Lists can be used instead
'''An array in Python is a data structure that can hold multiple items of the same type. 
While Python provides a native list type that can hold items of different types, 
the array is a more specialized construct requiring all items to be of the same type, 
which makes it efficient for certain numerical or scientific applications.
An array is a special variable, which can hold more than one value at a time.'''

cars = ["Ford", "Volvo", "BMW"] #same type
#we can use all list functions like add,remove,access to this array

###############################################
#sdatastructures
'''A data structure is a specialized format for organizing, processing, retrieving and storing data.
Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly.
'''
#4.	Data Structures
list=["sai","Gulivindala",2,3.5]
print(list)
list.pop(2)
print(list)

#slists
'''Built-in Data Structures
Lists
Lists are used to store data of different data types in a sequential manner. 
There are addresses assigned to every element of the list, which is called as Index.
The index value starts from 0 and goes on until the last element called the positive index.
There is also negative indexing which starts from -1 enabling you to access elements from the last to first. '''
import random
import time

servers = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

for server in servers:
    print(f"Pinging server: {server}...")
    
    success = random.choice([True, False])
    
    if success:
        print(f"Server {server} is reachable.")
    else:
        print(f"Failed to reach server {server}.")
    
    time.sleep(1)

print("Ping operation completed for all servers.")
'''Pinging server: 192.168.1.1...
Server 192.168.1.1 is reachable.
Pinging server: 192.168.1.2...
Failed to reach server 192.168.1.2.
Pinging server: 192.168.1.3...
Server 192.168.1.3 is reachable.
Pinging server: 192.168.1.4...
Failed to reach server 192.168.1.4.
Pinging server: 192.168.1.5...
Server 192.168.1.5 is reachable.
Ping operation completed for all servers.
'''
##############################################
#stuples
tuple1=("sai","Gulivindala",2,3.5,3+5j)
print(tuple1)
#tuple1[]
print(tuple1[1])
####################################################
Database_login = ("gmail","username","password")
Database_login.add("aadhar")
Database_login.remove("password") #if the user add additional data or remove existing data will get error
print(Database_login)
######################################################
# Tuple representing the immutable configuration of a Kubernetes deployment
k8s_deployment_config = ("default", "my-app-deployment", "nginx:latest")

# Accessing elements from the tuple
namespace, deployment_name, container_image = k8s_deployment_config

print(f"Kubernetes Deployment Configuration:")
print(f"Namespace: {namespace}")
print(f"Deployment Name: {deployment_name}")
print(f"Container Image: {container_image}")

# Trying to modify the tuple will raise an error
# k8s_deployment_config[0] = "production"  # Uncommenting this will raise a TypeError
##########################################################
#ssetdatastructure
container1 = {"nginx","busybox","nginx","grafana"}
container2 = {"nginx","helm","prometheus"}
#print(containers_create)#if want to create same name container it will take one container it deletes the duplicate one
containers_soft_both = container1 | container2
print(containers_soft_both)
containers_soft_common = container1 & container2
print(containers_soft_common)
diffrence_containers = container1 - container2
print(diffrence_containers)

############################################################
unique_ips = {"192.168.1.1", "192.168.1.2"}
unique_ips.add("192.168.1.3")
unique_ips.add("192.168.1.1")  # Duplicate, won't be added

print(f"UniqueIPs: {unique_ips}")
################################################################
#sdictionarydatstructure
dict = {"username": "saig","password":"Saigulivindala"}

print(dict)
##############################################################
server_status = {"aws":"running","jenkins": "stopped","kubernetes":"running"}

print(server_status["jenkins"])
server_status["jenkins"] = "running"
print(server_status["jenkins"])
####################################################################
branch_name = input()

git_branches = {
    "main": "a1b2c3d4e5f67890abcdef1234567890",
    "develop": "f0e1d2c3b4a5c6e7d8e9f0b1c2345678",
    "feature-branch": "d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8g9"
}
print(f"The latest commit on {branch_name} is: {git_branches[branch_name]}")

#########################################################################
#sarrayds
'''An array is a linear data structure that stores elements in contiguous memory locations. 
It allows for efficient indexing and iteration, making it ideal for scenarios 
where elements need to be accessed frequently and sequentially.'''
#seats selection in movie hall
seats_array=[
             ["A1","A2","A3"],
             ["B1","B2","B3"],
             ["C1","C2","C3"],
            ]
print(seats_array[1][2])
#############################################################################
#squeueds
from queue import Queue
import time
deployment_queue = Queue()

deployment_queue.put("Service-A")
deployment_queue.put("Service-B")
deployment_queue.put("Service-C")

while not deployment_queue.empty():
    service = deployment_queue.get()
    print(f"Deploying: {service}")
    time.sleep(2)  
    deployment_queue.task_done()

print("All deployments complete.")
#################################################################################
# Initialize a queue
queue = []
queue.append("task1")
queue.append("task2")
queue.append("task3")

# Process the queue in FIFO order
while queue:
    print(f"Processing first task in queue: {queue[0]}")
    queue.pop(0)  # Remove the first element


#################################################################################
#sseeinfoaboutmodule
'''from queue import Queue
import inspect
print(inspect.getmembers(Queue))

from queue import Queue
print(help(Queue))
'''
###################################################################################
#sstackds
from queue import LifoQueue as config_stack
import time

# Create a stack for configuration changes
#config_stack = LifoQueue()

def apply_change(resource, config_change):
    print(f"Applying change to {resource}: {config_change}")
    time.sleep(1)
    config_stack.put((resource, config_change))
    
apply_change("ConfigMap", "added one config data")
apply_change("Deployment", "Update image to v2.0")
apply_change("Service", "Add new endpoint")

def undo_changes():
    while not config_stack.empty():
        resource, config_change = config_stack.get()
        print(f"Undoing change on {resource}: {config_change}")
        time.sleep(1)
    print("All changes undone.")
print("\nError detected! Undoing changes...\n")
undo_changes()
######################################################################
browser_history = ["page1.html", "page2.html", "page3.html"]

while browser_history:
    print(f"Returning to last visited page {browser_history[-1]}")
    browser_history = browser_history[:-1]  # Remove the last page

'''Returning to last page page3.html
Returning to last page page2.html
Returning to last page page1.html'''


'''Returning page is page3.html
Returning page is page2.html
Returning page is page1.html'''
######################################################################
#slinkedlistds
import time

class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, name):
        self.stages.append(name)

    def execute(self):
        for name in self.stages:
            print(f"Executing stage: {name}")
            print(f"{name} in progress...")
            time.sleep(3)
        print("Pipeline execution completed.")

# Create and execute the pipeline
pipeline = Pipeline()
for stage in ["Build", "Test", "Deploy"]:
    pipeline.add_stage(stage)

pipeline.execute()


########################################################################
#5.	Classes and Objects (OOP)
#sclassesandobjects
'''In Python, a class is a blueprint for creating objects. 
It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have. 
Classes are a fundamental part of object-oriented programming (OOP), 
enabling you to encapsulate data and functions into reusable structures.'''


'''In Python, an object is an instance of a class. 
It is a fundamental building block in object-oriented programming (OOP) 
and represents a specific "thing" that has attributes (data) and behaviors (methods).'''
#createing a class
class Person:
    def __init__(self, name, age):
        # Attributes of the class
        self.name = name
        self.age = age

    # Method to introduce the person
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."


p = Person("sai", 25)  # Create an instance of the class
print(p.introduce())    # Output: Hi, my name is sai and I am 25 years old.

##################################################################################
#s__init__
'''In Python, the __init__ method is a special method that is automatically called when a new instance (object) of a class is created. 
It is known as the constructor of the class and is used to initialize the attributes of the new object.
The __init__ method can take additional arguments, allowing you to pass parameters when creating an instance. 
These parameters are typically used to set the initial state of the object.'''

#sselfparameter
'''The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
It does not have to be named self, you can call it whatever you like, 
but it has to be the first parameter of any function in the class'''
#Difference between Normal class method and __init__ method
class person:
    def setvalue(self,name,age):
        self.name = name  #instance attributes
        self.age = age
    
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")
p1=person()
name = input()
age = int(input())
p1.setvalue(name,age) #Without __init__, we have to manually set the attributes after the object is created:
p1.getvalue()

p2=person()
name = input()
age = int(input())
p2.setvalue(name,age)
p2.getvalue()
##################################
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")

name = input()
age = int(input())
p1=person(name,age)# Initialization happens automatically when the object is created.
p1.getvalue()


name = input()
age = int(input())
p2=person(name,age)
p1.getvalue()

#we can also update the properties ,delete properties and delete objects
p1.age=28
del p1.age
del p1

##################################################################
'''The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content,
 put in the pass statement to avoid getting an error.'''
 
 class sai:
    pass
#######################################################################
#s__init__
class CICDPipeline:
    def __init__(self, repo_url, branch, environment):
        """
        Initialize the pipeline configuration with repository URL, branch, and deployment environment.
        """
        self.repo_url = repo_url
        self.branch = branch
        self.environment = environment

    def checkout_code(self):
        """
        Simulate code checkout from the repository.
        """
        print(f"Checking out branch '{self.branch}' from repository '{self.repo_url}'.")

    def deploy_code(self):
        """
        Simulate deploying code to the specified environment.
        """
        print(f"Deploying code from branch '{self.branch}' to '{self.environment}' environment.")

    def run_tests(self):
        """
        Simulate running tests in the deployment environment.
        """
        print(f"Running tests on '{self.environment}' environment.")

# Example usage
pipeline = CICDPipeline(
    repo_url="https://github.com/example/myapp.git",
    branch="main",
    environment="production"
)

# Call methods to simulate pipeline tasks
pipeline.checkout_code()
pipeline.deploy_code()
pipeline.run_tests()
'''OUTPUT
Checking out branch 'main' from repository 'https://github.com/example/myapp.git'.
Deploying code from branch 'main' to 'production' environment.
Running tests on 'production' environment.
'''
####################################################################
#s__str__ method
'''In Python, the __str__ method is a special method used to define a string representation for an instance of a class. 
This method is called when you use the str() function or when you print the object using the print() function. 
The goal of __str__ is to provide a "nice" or user-friendly string representation of the object, which is meant to be readable.'''
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        
        return f"My name is {self.name} and my age is {self.age}"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
cls = MyClass(name,age)
print(cls)

'''we can also implement the __repr__ method in your class,
 which is intended to provide an official string representation of the object, often more suitable for debugging. 
If both methods are defined, __repr__ is typically aimed at developers, while __str__ is aimed at end users.'''

########################################################################
#sobjectmethods
'''Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:'''
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_fun(self):
        
        print("Hello my name is "+ self.name)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
p=MyClass("sai",25)
p.my_fun()

#####################################################################
'''OOPs Concepts in Python
OBJECT ORIENTED PROGRAMMING
 Object-oriented Programming is a way of approaching, designing and developing Software.
 oops is a programming paradigm that uses olojects and classes in the programe.
 It aims to implement real world entities like inheritance, polymorphism and encapsulation etc
 
 OOPs (Object-Oriented Programming) in Python is a programming paradigm that organizes code using objects and classes. 
 It allows developers to create modular, reusable, and scalable programs by modeling real-world entities as objects with attributes and behaviors. 
 Python supports OOP principles such as encapsulation, inheritance, polymorphism, and abstraction.
 
 Advantages of oops..
* Easier way to analyse and solve bugs
* Reusability of Code through inheritance
* Effective Problem Solving
* Elimination of Code redundancy.

Inheritance
Polymorphism 
Encapsulation 
Data Abstraction'''
#sInheritance
# Base class for Kubernetes resources
'''Inheritance in Python is a fundamental concept in object-oriented programming (OOP) that allows 
a class (called the child class or subclass) to inherit attributes and methods from another class (called the parent class or superclass).
 This mechanism promotes code reusability, as you can create new classes that are based on existing classes, 
 extending or modifying their behavior without needing to duplicate code.'''
 
 '''Parent Class (Superclass)
The parent class, also known as a superclass, is a class that provides properties (attributes) and methods (functions) that can be inherited by other classes. 
A parent class serves as a general template or blueprint from which child classes can derive their characteristics. 
It defines common functionality that can be shared across multiple child classes.'''

class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")
p=parent("sai",25)
p.info()

'''Child Class (Subclass)
A child class, also known as a subclass, is a class that inherits from a parent class. 
A child class can access the properties and methods of the parent class, and it can also add its own unique attributes and methods or override existing ones from the parent class. 
The child class is typically more specialized than the parent class.'''

class child(parent):
  pass
  
########################################################################
'''Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object.'''

#add the __init__() function to the child class:
class child(parent):
    def __init__(self,ph):
    
'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class child(parent):
    def __init__(self,ph):
        parent.__init__("sai",25)
        
'''Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent'''
class child(parents):
    def __init__(self,ph):
        super().__init__("sai",25)
'''By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.'''
#Then Add property to the child class
class child(parents):
    def __init__(self,ph):
        super().__init__("sai",25)
        self.ph=ph
'''In the above example, the ph 9392 should be a variable, and passed into the Student class when creating student objects.
 To do so, add another parameter in the __init__() function:''' 
class child(parents):
    def __init__(self,ph):
        super().__init__("sai",25)
        self.ph=ph
ch=child(9392)

#Add method
def mychild(self):
        print(f" My name is {self.name} and my age is {self.age}and phone number is {self.ph}")

'''If you add a method in the child class with the same name as a function in the parent class, 
the inheritance of the parent method will be overridden.'''    

class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

class child(parents):
    def __init__(self,ph):
        super().__init__("sai",25)
        self.ph=ph
    def mychild(self):
        print(f" My name is {self.name} and my age is {self.age} and phone number is {self.ph}")

p=parents("sai",25)
p.info()

ch=child(9392)
ch.mychild()

'''OUTPUT  
My name is sai and my age is 25
 My name is sai and my age is 25and phone number is 9392 '''  
 
'''Differences Between Using Parent and super()
1. Readability and Maintainability
With Parent: You are hardcoding the parent class name. 
If the parent class name changes (e.g., Parent is renamed to BaseClass), 
you'll need to update every occurrence of Parent in your child classes.

With super(): It dynamically resolves the method from the class hierarchy. 
You don’t need to change anything if the parent class name changes.'''

'''The super() function in Python is used to call methods from a parent (or superclass) in a child class. 
It provides a way to access the methods and properties of the parent class without explicitly naming it. 
This is especially useful in inheritance, particularly in cases of multiple inheritance, 
as it avoids hardcoding the parent class name and ensures the method resolution order (MRO) is followed correctly.'''

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

class Child(Parent):
    def __init__(self, name, age, ph):
        # Using super() to call the parent class's __init__ method
        super().__init__(name, age)
        self.ph = ph

    def mychild(self):
        print(f"My name is {self.name}, my age is {self.age}, and my phone number is {self.ph}")

# Create an instance of Parent
p = Parent("Sai", 25)
p.info()

# Create an instance of Child
ch = Child("Sanju", 27, 9392)
ch.mychild()

'''My name is Sai and my age is 25
My name is Sanju, my age is 27, and my phone number is 9392'''
#######################################################################
'''MRO (Method Resolution Order) in Python refers to the order in which Python searches for a method or attribute in a class hierarchy. 
It is the sequence Python follows to determine which method to call when multiple classes are involved, 
particularly in the case of inheritance.
The MRO ensures that:
Each class in the hierarchy is visited only once.
The order is consistent and follows a well-defined algorithm.
It prevents issues like duplicate method calls or skipping methods.'''
#MRO in Inheritance
'''Single Inheritance in Python
Single inheritance is a type of inheritance in which a child class inherits from only one parent class.
 This is the simplest form of inheritance and is used when a derived class needs to extend or 
 customize the functionality of a single base class.'''
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def show(self):
        print("Class C")

c = C()
c.show()  # Output: Class C

MRO: C -> B -> A -> object
Python starts searching for show() in class C, finds it, and stops.

###################################################################
#MRO in multiple inheritance
'''Multiple Inheritance in Python
Multiple inheritance is a feature of object-oriented programming where a class can inherit from more than one parent class. 
This allows the derived class to inherit attributes and methods from multiple base classes, 
combining their functionalities.'''
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

c = C()
c.show()  # Output: Class A

MRO: C -> A -> B -> object
Python searches C, then A, then B.

#############################################################
'''Multilevel Inheritance in Python
Multilevel inheritance refers to a scenario where a class inherits from a derived class, creating a chain of inheritance. 
For example, Class A is the base class, Class B inherits from Class A, and Class C inherits from Class B. 
This chain can extend to any number of levels.'''

class Grandparent:
    def display_grandparent(self):
        print("This is the Grandparent class")

class Parent(Grandparent):
    def display_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def display_child(self):
        print("This is the Child class")

# Creating an instance of the Child class
c = Child()

# Accessing methods from all levels of the hierarchy
c.display_grandparent()  # Inherited from Grandparent
c.display_parent()       # Inherited from Parent
c.display_child()        # Defined in Child
########################################################################
'''Hierarchical Inheritance in Python
Hierarchical inheritance is a type of inheritance where multiple child classes inherit from the same parent class. 
In this scenario, a single parent class acts as the base class for multiple derived classes.'''

class Parent:
    def display_parent(self):
        print("This is the Parent class")

class Child1(Parent):
    def display_child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def display_child2(self):
        print("This is Child2 class")

# Creating instances of child classes
c1 = Child1()
c2 = Child2()

# Accessing parent and child methods
c1.display_parent()  # Inherited from Parent
c1.display_child1()  # Defined in Child1

c2.display_parent()  # Inherited from Parent
c2.display_child2()  # Defined in Child2

#########################################################################
'''Hybrid Inheritance in Python
Hybrid inheritance is a combination of two or more types of inheritance in a class hierarchy. 
It involves a mix of single, multiple, multilevel, or hierarchical inheritance patterns. 
Hybrid inheritance is used to model complex relationships among classes while ensuring code reusability and flexibility.'''

class Grandparent:
    def display_grandparent(self):
        print("This is the Grandparent class")

class Parent1(Grandparent):
    def display_parent1(self):
        print("This is Parent1 class")

class Parent2(Grandparent):
    def display_parent2(self):
        print("This is Parent2 class")

class Child(Parent1, Parent2):  # Multiple inheritance
    def display_child(self):
        print("This is the Child class")

# Creating an instance of the Child class
c = Child()

# Accessing methods from all classes
c.display_grandparent()  # Inherited from Grandparent
c.display_parent1()      # Inherited from Parent1
c.display_parent2()      # Inherited from Parent2
c.display_child()        # Defined in Child

########################################################################
class K8sResource:
    def __init__(self, name, namespace):
        """
        Initialize the Kubernetes resource with name and namespace.
        """
        self.name = name
        self.namespace = namespace

    def get_details(self):
        """
        Simulate retrieving resource details.
        """
        return f"Resource: {self.name}, Namespace: {self.namespace}"

# Derived class for Deployment management
class Deployment(K8sResource):
    def scale(self, replicas):
        """
        Simulate scaling the deployment.
        """
        print(f"Scaling deployment '{self.name}' to {replicas} replicas in namespace '{self.namespace}'.")

# Derived class for Service management
class Service(K8sResource):
    def expose(self, port):
        """
        Simulate exposing the service on a specific port.
        """
        print(f"Exposing service '{self.name}' on port {port} in namespace '{self.namespace}'.")

# Example usage
# Create a Deployment instance
deployment = Deployment(name="my-app", namespace="production")
print(deployment.get_details())
deployment.scale(replicas=3)

# Create a Service instance
service = Service(name="my-app-service", namespace="production")
print(service.get_details())
service.expose(port=8080)

'''OUTPUT:
Resource: my-app, Namespace: production
Scaling deployment 'my-app' to 3 replicas in namespace 'production'.
Resource: my-app-service, Namespace: production
Exposing service 'my-app-service' on port 8080 in namespace 'production'.
'''
############################################################################       
#spolymorphism
'''*Polymorphism means having many forms
* In Simple words, we can define polymorphism as the ability of a more than message to be displayed in one form.
* A real life example of Polymorphism who at the Same time Characteristics. is a person Can have different
* Polymorphism in Pythan allow us to define methods in child class with the name as Same defined in their parent class.

Two Types Of Polymorphism:
1.Run-Time Polymorphism (Dynamic Polymorphism): Achieved through method overriding and is resolved during execution. 
It allows objects of different classes to be treated as objects of a common superclass.

a.Method Overriding in Python:
Method overriding is a feature in object-oriented programming where a subclass provides a specific 
implementation for a method that is already defined in its parent class. 
In Python, it allows a child class to modify or extend the behavior of methods inherited from the parent class.
if you want to implement Mehod Overriding Method name should be same and no of arguments should be same in both the classess

Inheritance Required:

Method overriding occurs in the context of a subclass inheriting from a parent class.
Same Method Signature:

The overriding method in the subclass must have the same name and parameters as the method in the parent class.
Dynamic Behavior:

When an overridden method is called on an object of the subclass, the subclass version is executed.
super() for Parent Method:

The super() function allows access to the overridden method in the parent class, 
enabling the subclass to extend the functionality of the parent method.'''

#Basic Example of Method Overriding:
class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def greet(self):
        print("Hello from the Child class!")

# Instantiate objects
parent = Parent()
child = Child()

# Call the greet method
parent.greet()  # Output: Hello from the Parent class!
child.greet()   # Output: Hello from the Child class!

#Using super() function

class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def greet(self):
        super().greet()  # Call the parent class's greet method
        print("Hello from the Child class!")

# Instantiate child object
child = Child()
child.greet()

# Output:
# Hello from the Parent class!
# Hello from the Child class!

##################################################################
'''Overriding __init__ Method:
The __init__ method can also be overridden in a subclass, often to initialize additional attributes. 
The parent class's __init__ method can be invoked using super().'''

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Initialize the name attribute from Parent
        self.age = age

# Instantiate child object
child = Child("Alice", 10)
print(child.name)  # Output: Alice
print(child.age)   # Output: 10

###########################################
class Parent:
    def __init__(self,name):
        self.name=name
        print("parents method")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
child=Child("sai",25)
print(child.name)
print(child.age)


#parents method,name,age


'''2.Compile-Time Polymorphism (Static Polymorphism): Achieved through method overloading and 
operator overloading, resolved during compilation.where methods are resolved at compile time

Compile-time polymorphism, often referred to as static polymorphism, allows for method overloading and operator overloading. 
This is resolved at compile time, meaning the correct method is determined before the program starts running.

Method Overloading: Methods in the same class have the same name 
but different parameters (though Python does not natively support method overloading as seen in languages like Java or C++).
Python does not natively support method overloading. 
because it uses dynamic typing and interprets the latest method definition as the active one.Instead, 
we can achieve similar behavior using default arguments or variable-length arguments (*args, **kwargs).'''

class Calculator:
    def add(self,*args):
        if len(args) == 0:
            print("No arguments provides")
        elif len(args) == 1:
            print(f"one argument is provide: {args[0]}")
        else:
            print(f"sum of arguments is: {sum(args)}")
calc=Calculator()
calc.add()
calc.add(1)
calc.add(1,2,3)


'''Operator Overloading: Python allows you to define or change the behavior of operators for user-defined classes.
Operator overloading in Python allows developers to define or modify the behavior of operators (+, -, *, etc.) 
for custom objects by overriding special methods (also called magic methods or dunder methods). '''

def operator(a,b):
    print(a+b)
operator(4,5) #add integers
operator("Sai","Gulivindala") #concate strings
operator([1,2,3],[4,5,6]) #add items


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self,other ):
        return Point(self.x + other.x, self.y + other.y)

    # String representation for easier display
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)

result = p1 + p2  # Overloading '+' operator
print(result)  # Output: Point(4, 6)

s1="sai"
s2="gulivindala"
print(s1+s2)


self.x + other.x = 2 + 4 = 6  #self is current instance(p1)  other is right hand side (p2) 
self.y + other.y = 3 + 5 = 8

'''__str__ Method:
Added the __str__ method to provide a readable string representation of the Point object, so when you print it, you get something meaningful like Point(6, 8)'''
######################################################   

'''
Function Polymorphism
An example of a Python function that can be used on different objects is the len() function.

1.String
For strings len() returns the number of characters:'''
x = "sai"
print(len(x))
'''2.Tuple
For tuples len() returns the number of items in the tuple:'''

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
print(len(x))

'''3.Dictionary
For dictionaries len() returns the number of key/value pairs in the dictionary:'''

thisdict = {
  "brand": "VIVO",
  "model": "T2 5g",
  "year": 2024
}

print(len(thisdict))

######################################################################################
#sclassploymorphism

'''Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()'''

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")

car1=Car("TATA","I10")
boat1=Boat("sai","v6model")
plane1=Plane("Boeing","747")

for i in (car1,boat1,plane1):
    i.move()
        
 #######################################################################
#sinheritancepolymorphism 
'''Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, 
the child classes inherits the Vehicle methods, but can override them:
'''
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("sail")
class Plane(Vehicle):
    def move(self):
        print("Flyy")

car1=Car("TATA","I10")
boat1=Boat("sai","v6model")
plane1=Plane("Boeing","747")

for i in (car1,boat1,plane1):
    print(i.brand)
    print(i.model)
    i.move()
############################################################# 
class CloudProvider:
    def deploy_instance(self):
        raise NotImplementedError

class AWSProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching EC2 instance in AWS"

class AzureProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching Virtual Machine in Azure"

class GCPProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching Compute Engine instance in GCP"

def provision_cloud_instance(provider: CloudProvider):
    print(provider.deploy_instance())

# Real-time polymorphism
providers = [AWSProvider(), AzureProvider(), GCPProvider()]
for provider in providers:
    provision_cloud_instance(provider)
    

'''OUTPUT
Launching EC2 instance in AWS
Launching Virtual Machine in Azure
Launching Compute Engine instance in GCP
'''

'''Dynamic Typing in Python
Dynamic typing is a feature of programming languages like Python where the type of a variable is determined at runtime 
rather than being explicitly declared or fixed during compile time. 
In other words, variables in Python do not have a fixed type, and their type can change depending on the value assigned to them.
'''
#############################################################################################
#sencapsulation

'''Encapsulation is a fundamental concept in object-oriented programming (OOP) that restricts direct access to some of an object's components, which can prevent the accidental modification of data. 
In Python, encapsulation is achieved using the concept of classes and access modifiers
 It is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit called a class.

1.Data Hiding:

Encapsulation allows data to be hidden from the outside world.
The data can only be accessed and modified through well-defined methods (getters and setters).

2.Access Modifiers in Python:

Python provides three levels of access control for attributes and methods:
1.Public: Accessible from anywhere (attribute_name).
Public members can be accessed from anywhere, both inside and outside the class.
No special syntax is required for public members.'''

class Person:
    def __init__(self, name):
        self.name = name  # Public member
person = Person("Alice")
print(person.name)  # Accessible from outside


''''2.Protected: 
Accessible within the class and its subclasses (_attribute_name).
Protected members are intended to be accessible only within the class and its subclasses.
By convention, they are prefixed with a single underscore _.
This is a convention, not enforcement. It signals to other developers that the member is for internal use.'''

class Person:
    def __init__(self, name, age):
        self._age = age  # Protected member
person = Person("Alice", 30)
print(person._age)  # Still accessible but discouraged,not recommmended approach

'''Encapsulation Breach: Accessing _protected_member directly bypasses the abstraction and encapsulation intended by the class design.'''
#Recommended way
class Person:
    def __init__(self, name, age):
        self._age = age  # Protected member

    def get_age(self):
        return self._age  # Controlled access to the protected member

person = Person("Alice", 30)
print(person.get_age())  #Output: 30


######################################################################################
'''3.Private: Accessible only within the class (__attribute_name).
Private members are intended to be accessible only within the class.
They are prefixed with a double underscore __, which triggers name mangling to make the member harder to access from outside the class.
This does not provide absolute security but makes accidental modification less likely.
'''
class Person:
    def __init__(self, name, age):
        self.__age = age  # Private member
    
    def get_age(self):
        return self.__age  # Accessor method

person = Person("Alice", 30)
# print(person.__age)  # Raises AttributeError
print(person.get_age())  # Access through a method

'''4. Getters and Setters
Python allows defining getter and setter methods for controlled access to private or protected members.
These methods can validate or modify the values before assigning or retrieving them.'''

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0:
            self.__age=age
        else:
            raise ValueError("age must be positive")
p=Person("sai",25)
print(p.get_age())
p.set_age(26)
print(p.get_age())

'''5. Using Properties (@property)
Python provides a more Pythonic way of using getters and setters via the @property decorator.
This allows you to access methods like attributes while maintaining encapsulation.'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

p = Person("sai", 25)
print(p.age)  # Calls the getter
p.age = 26   # Calls the setter
print(p.age)  # Calls the getter again


###############################################################
#sdataabstraction
'''4.Data abstraction in Python is a key concept in object-oriented programming (OOP) that involves hiding the internal details 
and complexities of how data is represented or implemented, while exposing only the essential features. 
This allows developers to work with data in a simplified and consistent way, focusing on what data represents rather than how it is managed.
 It focuses on revealing only the relevant attributes and behaviors of an object while keeping the implementation details hidden. 
 This helps in reducing code complexity and increases the reusability of code.'''
 
 '''Python achieves data abstraction through:

1. Classes and Objects:
A class serves as a blueprint for creating objects. It encapsulates data (attributes) and functions (methods) to operate on that data.
By exposing only necessary details through methods and keeping some internal workings private, a class provides abstraction.'''

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # To be defined in subclasses

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog("Buddy")  #we are passing Dog name 
print(dog.make_sound())  # Output: Woof!

'''#Here, the user interacts with make_sound without knowing the internal implementation for each animal
#You can easily extend the functionality by adding more subclasses without modifying the Animal class
#The base class defines the common interface, while derived classes provide their specific behaviors.'''
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

cow = Cow("Daisy")
print(cow.make_sound())  # Output: Moo!

'''2.Encapsulation:
Encapsulation is the practice of bundling the data and methods that operate on the data into a single unit.
Python uses naming conventions to simulate private attributes. Attributes prefixed with _ or __ are considered non-public.'''

class BankAcount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
            
acount=BankAcount(1000)
print(acount.get_balance()) #1000

#print(acount.__balance)   #raise an Attribute error
acount.deposit(500)
print(acount.get_balance()) #1500

acount.withdraw(200)
print(acount.get_balance()) #1300

'''This makes it inaccessible directly from outside the class, enforcing that it can only be accessed 
or modified through specific methods provided by the class (e.g., deposit, withdraw, get_balance).'''


######################################################################################################
#6.	Modules and Packages
#7.	Error Handling and Exceptions
#8.	File Handling
#9.	Iterators and Generators
#siterators
'''In Python, an iterator is an object that allows you to traverse through a collection 
(like a list or a dictionary) one element at a time. 
Iterators implement two special methods defined by the iterator protocol: __iter__() and __next__().
1.
__iter__(): This method returns the iterator object itself. It is required for an object to be considered an iterator.

__next__(): This method returns the next value from the iterator. 
When there are no more elements to return, it raises the StopIteration exception to signal the end of the iteration.

2.Creating an Iterator:
You can create your own iterator by defining a class that implements the __iter__() and __next__() methods.
'''

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# Example of using the iterator
my_list = [1, 2, 3, 4]
iterator = MyIterator(my_list)

for item in iterator:
    print(item)
###############################################################

''' 3.Built-in Iterators
Python has several built-in iterable types, such as lists, tuples, sets, and dictionaries. 
You can easily get their iterators using the iter() function'''

my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration
####################################################################
'''4.Using Generators
A common and more concise way to create iterators is by using generators. 
Generators are a simple way to create iterators using the yield statement:'''
def my_generator(data):
    for item in data:
        yield item

# Example usage
for item in my_generator([1, 2, 3]):
    print(item)
###########################################################################
'''5. Iteration in Python
You can use the built-in for loop to iterate over any iterable (which is anything that can 
return an iterator, such as lists, sets, tuples, etc.).'''
############################################################################
#sscope
#A variable is only available from inside the region it is created. This is called scope.

'''Local Scope:
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.'''

def myfunc():
  x = 300
  print(x)

myfunc()

'''Global Scope:
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.'''
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

'''Naming Variables
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, one available in the global scope 
(outside the function) and one available in the local scope (inside the function):'''

x = 300

def myfunc():
  x = 200
  print(x) #200

myfunc()

print(x) #300

'''Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
'''

def myfunc():
  global x
  x = 300

myfunc()

print(x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

'''Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.

If you use the nonlocal keyword, the variable will belong to the outer function:'''

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

###############################################################################################
#smodule
'''In Python, a module is a file that contains Python code, typically used to organize and reuse code. 
Modules can define functions, classes, and variables, as well as include runnable code. 
By grouping related code into a module, you can make your programs more organized and modular.'''

'''Create a Module
To create a module just save the code you want in a file with the file extension .py:
'''
#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
  
'''Use a Module
Now we can use the module we just created, by using the import statement:'''  
#Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("sai")

'''Variables in Module
The module can contain functions, as already described, 
but also variables of all types (arrays, dictionaries, objects etc)'''
#Save this code in the file mymodule.py

person1 = {
  "name": "sai",
  "age": 36,
  "country": "India"
}

import mymodule

a = mymodule.person1["age"]
print(a)
###############################
import mymodule as sai

a = sai.person1["age"]
print(a)

#Built in modules
import platform

x = platform.system()
print(x)

#################################
'''Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:'''

import platform

x = dir(platform)
print(x)
###################################
'''Import From Module
You can choose to import only parts from a module, by using the from keyword.'''
#The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "sai",
  "age": 25,
  "country": "India"
}

#Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])

#############################################
#spythondates
'''Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.'''
import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)    #2025
print(x.strftime("%A")) #Monday

'''The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:'''

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #June
#################################################
#smathmodule
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

Example
x = abs(-7.25)

print(x)

####################################################
x = pow(4, 3)

print(x)

import math

x = math.sqrt(64)

print(x)
############################################################
'''The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method 
rounds a number downwards to its nearest integer, and returns the result:'''
'''Python has a set of built-in math functions, including an extensive math module, 
that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:'''

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

####################################################################

'''JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.

'''

#Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

'''Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.'''

#Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

###########################################################
#Convert a Python object containing all the legal data types:

import json

x = {
  "name": "sai",
  "age": 25,
  "married": True,
  "divorced": False,
  "children": ("sai","sandy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#{"name": "Jsai", "age": 25, "married": true, "divorced": false, "children": ["sai","sandy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]

######################################################################################################
json.dumps(x, indent=4)

#result will be
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
    
#################################################################################################
#sregularexpressions
'''Python RegEx:
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:
'''
##################################################################################################
#10.Comprehensions
#11. Decorators and Closures
#12. Regular Expressions
#13. Multithreading and Multiprocessing
#14. Networking
#15. Database Interaction
#16. Data Science and Visualization (Popular Libraries)
#17. Web Development
#18. Testing and Debugging
#19. Version Control with Git
#20. Advanced Topics
#21. Python Tools and Best Practices
