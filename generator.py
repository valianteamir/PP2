def generator(n):
    for i in range(0,n+1):
        yield (i*i)
for i in generator(5):
    print(i) #1
    
def gen(n):
    for i in range(n):
        if i%2==0:
            yield i 
n=int(input())
even_nums=gen(n)
for a in even_nums:
    print(a,end=",") #2

def div_by_3_and_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i #3
            
def squares(nums):
    for i in nums:
        yield (i*i)
nums=[10,11,12,13,14,15]
square_nums =  squares(nums)
for num in square_nums:
    print (num) #4
    
def revese_count(n):
    for i in range(n,0,-1):
        yield i
    else:
        yield 0
for a in revese_count(25):
    print(a,end=" ") #5