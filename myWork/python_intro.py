print("Hello World")

# fast easy comment
'this is also a comment'
'''
this can take several lines of comments
used for describing functions or 
classes
'''
# Variables
x = 100
y = 5.5
x = [1,2,3]
x = 'hello'
intx = 100
inty = 10
result = intx/inty
print(result)
result = int(result)
print(result)
result = intx // inty
print(result)

# Math module
min_val = min(10,1)
print(min_val)
raised = pow(2,4)
print(raised)
raised = 2**4
print(raised)

# if statements
x = -1
y = 1
if x < 0:
    print('x < 0')
if x < 0 and y > 0:
    print('values within range')
if x < 0 or y > 0:
    print('at least one value in range')
if x < 0 :
    print('x')
elif x > 0 :
    print('x > 0')
else:
    print('x is 0')

# Loops
counter = 0
while counter < 10:
    print(counter)
    counter += 1
a_list = [1,2,3,4,5]
for i in range(5):
    print(i, a_list[i])

for i in range(len(a_list)):
    print(a_list[i], end=" ")
print()

for i, val in enumerate(a_list):
    print(i, val)
for val in a_list:
    print(val)

# functions
def hello(name = "Alice"):
    print("Hello", name)
hello("Tom")

f_name = "Liam"
l_name = 'Baker'
full_name = f_name + " " + l_name
print(full_name)
first_char = full_name[0]
print(first_char)
last_char = full_name[-1]
print(last_char)

# Slicing
slF = full_name[:4]
slL = full_name[5:]
print(slF)
print(slL)
# rn = "React Native"
# react = rn[:5]
# print(react)
# native = rn[6:]
# print(native)