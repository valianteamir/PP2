import os
path = r"/Users/amirdank/Desktop/test/"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
print(dir_list)

print("Directories in '", path, "' :")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])

print("Files in '", path, "' :")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) # 1

import os
print('Exist:', os.access(r'/Users/amirdank/Desktop/PP2/builtin_functions.py', os.F_OK))
print('Readable:', os.access(r'/Users/amirdank/Desktop/PP2/builtin_functions.py', os.R_OK))
print('Writable:', os.access(r'/Users/amirdank/Desktop/PP2/builtin_functions.py', os.W_OK))
print('Executable:', os.access(r'/Users/amirdank/Desktop/PP2/builtin_functions.py', os.X_OK)) #2


PathName = input("Enter yout path:")
path = r"{}".format(PathName)
if os.path.exists(path): 
    print("Your path exists")
    print("Filename of the path: {}".format(os.path.basename(path)))
    print("Directory of the path: {}".format(os.path.dirname(path))) #3
else: print("Your path doesn't exist ")

f= open("test.txt", "r")
cnt = 0
for line in f: cnt+=1
print(cnt) # 4

l = [1,2,3,4,5]
with open("test.txt", "w+") as f:
    for i in l:
        f.write(str(i)) #5
        
# for i in range(65, 91):
#         f = open(r"/Users/amirdank/Desktop/PP2/A-Z-files/{}.txt".format(chr(i)), "x") #6

# with open("test.txt") as f:
#     with open('copy.txt', "w") as cop:
#         for line in f:
#             cop.write(line) #7
# path = r"/Users/amirdank/Desktop/PP2/copy.txt"
# if not os.path.exists(path=path):
#     print("The path Doesn't exist")

# os.remove(path)





