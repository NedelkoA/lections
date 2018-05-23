from hashlib import md5
import datetime

def hash_md5(str1):
    return md5(str1.encode())


class Greeter:
    def greet(self, name):

        name = name.replace(' ', '')
        name = name.title()
        date = datetime.datetime.time(datetime.datetime.now())
        print(date.hour)
        if 12 > date.hour and 6 < date.hour:
            return "Good morning " + name
        elif 22 > date.hour and 18 < date.hour:
            return "Good evening " + name
        elif 6 > date.hour and 22 < date.hour:
            return "Good night " + name
        return "Hello " + name


# print(datetime.now())
# print(datetime(2018, 5, 23, 12, 30))
# if datetime.now() < datetime(2018, 5, 23, 12, 30):
#     print(1)

#print(datetime.time(datetime.now()).hour)
gr = Greeter()
print(gr.greet("ivan"))