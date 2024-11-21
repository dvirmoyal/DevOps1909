from cgi import print_environ

from setuptools.extern import names

a = "aviel"
i = 1
while i <=5 :
    print(a)
    i=i+1
print(list(range(5)))
print(list(range(1,50,10)))
print(list(range(50,10,-3)))
names = ["dvir", "adi", "tal"]
for name in names:
    if name == "dvir":
        name = "roey"
    print("hello " + name)
for i in range(len(names)):
    if names[i] == "dvir":
        names[i] = "roey"
    print("hello " + names[i])
for i in range(5):
    print(a)