from datetime import datetime, timedelta 
t1 = datetime.now()
t2 = timedelta(5)
t3 = t1 - t2
print(t3.strftime("%d-%m-%y")) #1

t1 = datetime.now()
day = timedelta(1)
print((t1 - day).strftime("%d-%m-%y"))
print(t1.strftime("%d-%m-%y"))
print((t1 + day).strftime("%d-%m-%y")) #2

t = datetime.now().replace(microsecond=0)
print(t) #3

def difference_inSeconds(date_2,date_1):
    timedelta=date_2-date_1
    return timedelta.days *24 *3600 + timedelta.seconds
date_1= datetime(2019, 4, 18, 11, 3, 5)
date_2=datetime.now()

print(difference_inSeconds(date_2,date_1),"seconds")
# 4


