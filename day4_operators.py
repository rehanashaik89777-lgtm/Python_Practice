# Arithmetic Operators
a = 20
b = 6

add=a+b
sub=a-b
mul=a*b
div=a/b
floor_div=a//b
rem=a%b
pow=a**b

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Floor Division:", floor_div)
print("Remainder:", rem)
print("Power:", pow)


#operator prediction

print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 // 6)
print(20 % 6)
print(2 ** 4)


# Assignment Operators
x = 10
x+= 5
x-= 5
x*= 5
x/= 5
print("x+= 5:", x+5)
print("x-= 5:", x-5)
print("x*= 5:", x*5)
print("x/= 5:", x/5)


# Comparison Operators
age = 20
print(20>18)
print(20<18)
print(20==20)
print(20!=25)
print(20>=18)

# Logical Operators
age = 20
print(age>18 and age<30)
print(age>18 or age<30)
print(not(age>18 and age<30))

# Real Life Example
marks = 75
attendence = 80
print(marks>40)
print(attendence>=75)
if marks>40 and attendence>=75:
    print("Both requirements are satisfied")