import re
txt = input()
x = re.search(".ab*", txt)
print ('Match found') if x else print('Match not found') #1 a by one or more b's

txt = input()
x = re.search("a(b){2,3}", txt)
print ('Match found') if x else print('Match not found') #2 a followed by two or three bs

txt = input()
x = re.findall("[a-z]+_[a-z]+", txt)
print(x)
print ('Match found') if x else print('Match not found') #3 sequence of lowercase split by underscore

txt = input()
x = re.findall("[A-Z][a-z]+", txt)
print(x)
print ('Match found') if x else print('Match not found') #4 uppercase followed by lower case

txt = input()
x = re.search("a.*b$", txt)
print ('Match found') if x else print('Match not found') #5 a followed by anything ending in b

txt = input()
x = re.sub('[ ,.]' , ':', txt) 
print (x) #6 replace all occurences of space, comma or dot with a colon

txt = input()
res = re.sub(r'(?:^|_)(.)', lambda x: x.group(1).upper(), txt)
print(res) #7 snake to camel
 

txt = input()
pattern=r'([A-Z])'
print(re.split(pattern,txt)) #8 split at uppercase

txt= input()
pattern='([A-Z])'
print(re.sub(pattern,r' \1',txt)) #9 insert spaces

txt= input()
pattern=r'([A-Z])'
print(re.sub(pattern,r'_\1',txt).lower()) #10 #helloMyBro camel to snake
