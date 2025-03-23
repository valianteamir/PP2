from time import sleep
import math

def multiply (list):
    print(math.prod(list))
list=[10,2,4,6]
multiply(list) # 1

string = input()
lower = sum([1 for i in string if i.islower()])
upper = sum([1 for k in string if k.isupper()])

print(lower, upper) #2

myString = input()
print(myString[::-1]==myString) #3



def delay(fn, ms, *args):
  sleep(ms/1000)
  return fn(*args)
fn = int(input())
ms = int(input())
print(f'Square root of {fn} after {ms} specific miliseconds:') 
print(delay(lambda x: math.sqrt(x), ms, fn)) #4

myTuple = (1, 1, 1, 1)
print(all(myTuple)) #5 

