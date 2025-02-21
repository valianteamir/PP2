import math 
n = int(input("Input degree: "))
p = math.pi
r = n * p/180
print(r)
# or
# print(math.radians(n)) 1

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
x = (a + b)*h/2
print(x) # 2

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
x = a**2 * n / (4 * math.tan(math.pi/n))
print(int(x)) # 3

l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
s = l * h
print(float(s)) #4
