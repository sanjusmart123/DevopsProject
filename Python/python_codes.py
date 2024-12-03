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
#2.	Control Flow Statements
#sif elif else :
lastball = 4
if lastball >= 6:
    print("Won the match")
elif lastball == 5:
    print("Draw match")
else:
    print("Lost the match")
    
#snestedif

branch_name=input()
build_status =input()
if branch_name == "develop":
    if build_status == "success":
        print("deploying to staging env")
    else:
        print("build failed,Not deploying to staging")
elif branch_name == "master":
    if build_status == "success":
        print("deploying to production")
    else:
        print("build failed,Not deploying to production")
        
else:
    print("deploying to feature branch,no deployment triggered")
######################################################################   
import os
print("File exists") if os.path.exists("/home/usr/sai.txt") else print("File does not exist")
#Checks if the file exists at the specified path.

import os
for file_path in ["/home/usr/devops.txt","/home/usr/aws.txt","/home/usr/kubenernetes.txt"]: print(f"{file_path} exists" if os.path.exists(file_path) else f"{file_path} does not exists")

import os
print("all files exists") if all(os.path.exists(file) for file in ["/home/usr/pyhton.txt","/home/usr/devops.txt","/home/usr/aws.txt"]) else print("some files missing")

#soneline_if_elif_else
server_status = int(input())
status = "up" if server_status ==1 else "down" if server_status ==0 else "unknown"
print(status)

#sfor loop
sai=75
for memory in range(sai):
    if memory >= 70:
        break
    elif memory < 70:
        print("its ok")
        break
        
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
'''jenkins_url: The base URL of the Jenkins server (e.g., http://jenkins.example.com).
token: A token used for authentication to trigger the job. 
This is typically generated within Jenkins for security.
Jenkins' REST API provides a way to trigger jobs via the /build endpoint
requests.post(): Sends a POST request to the URL to trigger the Jenkins job.
requests is a popular Python library for making HTTP requests.'''
##########################################
def greet(name):
    message = f"Good Morning, {name}"
    return message

print(greet("sai"))
print(greet("sai gulivindala"))

###############################################

#4.	Data Structures
list=["sai","Gulivindala",2,3.5]
print(list)
list.pop(2)
print(list)

tuple1=("sai","Gulivindala",2,3.5,3+5j)
print(tuple1)
#tuple1[]
print(tuple1[1])

Database_login = ("gmail","username","password")
Database_login.add("aadhar")
Database_login.remove("password") #if the user add additional data or remove existing data will get error
print(Database_login)

container1 = {"nginx","busybox","nginx","grafana"}
container2 = {"nginx","helm","prometheus"}
#print(containers_create)#if want to create same name container it will take one container it deletes the duplicate one
containers_soft_both = container1 | container2
#print(common_soft)
containers_soft_common = container1 & container2
print(containers_soft_common)
print(containers_soft_both)

#dict = {"username": "saig","password":"Saigulivindala"}

#print(dict)

server_status = {"aws":"running","jenkins": "stopped","kubernetes":"running"}

print(server_status["jenkins"])
server_status["jenkins"] = "running"
print(server_status["jenkins"])


#5.	Classes and Objects (OOP)

class person:
    def setvalue(self,name,age):
        self.name = name
        self.age = age
    
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")
p1=person()
name = input()
age = int(input())
p1.setvalue(name,age)
p1.getvalue()

p2=person()
name = input()
age = int(input())
p1.setvalue(name,age)
p1.getvalue()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")

name = input()
age = int(input())
p1=person(name,age)
p1.getvalue()


name = input()
age = int(input())
p2=person(name,age)
p1.getvalue()

        

#6.	Modules and Packages
#7.	Error Handling and Exceptions
#8.	File Handling
#9.	Iterators and Generators
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


