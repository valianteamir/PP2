import re
# txt = input()
# x = re.search(".*ab+", txt)
# print ('Match found') if x else print('Match not found') #1

# txt = input()
# x = re.search("a(b){2,3}", txt)
# print ('Match found') if x else print('Match not found') #2

# txt = input()
# x = re.findall("[a-z]+_[a-z]+", txt)
# print(x)
# print ('Match found') if x else print('Match not found') #3

# txt = input()
# x = re.findall("[A-Z][a-z]+", txt)
# print(x)
# print ('Match found') if x else print('Match not found') #4

# txt = input()
# x = re.search("a.*b$", txt)
# print ('Match found') if x else print('Match not found') #5

# txt = input()
# x = re.sub('[ ,.]' , ':', txt)
# print (x) #6

# txt = input()
# res = re.sub(r'(?:^|_)(.)', lambda x: x.group(1).upper(), txt)
# print(res) #7
 

# text = input()
# pattern=r'([A-Z])'
# print(re.split(pattern,text)) #8

# text= input()
# pattern='([A-Z])'
# print(re.sub(pattern,r' \1',text)) #9

text= input()
pattern=r'([A-Z])'
print(re.sub(pattern,r'_\1',text).lower()) #10 #helloMyBro
