'''

#Defaultdict
from collections import defaultdict

def def_value():
    return "Not present"
d = defaultdict(def_value)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

'''





'''
 #I/O files

#To get current directory
pwd

%%writefile myfile.txt
Hello, this is a text file
this is second line
this is third line

myfile = open('myfile.txt')
myfile.read()
myfile.seek(0)

#To get each sentence as a string in list
myfile.readlines()

#To ensure the protection of the file
myfile.close()

#Using with you don't have to ensure closing the file
with open('myfile.txt') as my_file:
    contents = my_file.read()
    
#Reading, writing, appending modes
- mode = 'r' is read only
- mode = 'w' is write only (will overwrite files)
- mode = 'a' is append only (will add on to files)
- mode = 'r+' is reading and writing
- mode = 'w+' is writing and reading
'''





'''
- Passing function as a input value
- Get the return value of function in a variable

def abc():
    return 3
a = abc()

def xyz(i);
    return i
xyz(a)
'''


'''
*args (* is denotion and args can be any keyword) - specifying mutiple parameters while calling the function 
**kwargs (** is the dention and while calling the function it can be called as fruit = 'orange')

Eg:

def myfunc(*args,**kwargs):
    print(args[3])
    print(kwargs['fruit'])
    
myfunc(10,20,30,fruit = 'orange',veggie = 'cauliflower')
'''

'''
#Reduce
import functools
print(((functools.reduce(lambda a,b : a/b,[3,5,2,6]))))

# filter
print(list(filter(lambda x : x%2 == 0, [2,3,5])))

#map
'''



'''
# Global keyword is used to create a global variable which can be accessed only outside the local scope (bar())
x = 20

def bar():
    global x
    x = 25
    return x

print("Before calling bar: ", x)
print("Calling bar now")
bar()
print("After calling bar: ", x)

'''


'''
from package import module

Package - Directory/Folder
Module - (Py) file

To create your own Package , create a folder and create an init file there.
And then create the py file (module) inside that.
'''


'''
__init__ and __main__

Purpose : To know if the file is executed directly or through another program using import statement.

Initially __init__ is set __main__.
if __init__ == '__main__':
    print('Executed directly')
else:
    print('Executed through import')
'''


'''
Exception Handling
try:
    result = int(input('Enter a number'))
#Will be executed if try block fails
except:
    print('Whoop! That is not a number')
    continue
#Will be executed if condition passes doesn't really go into except
else:
    print('It is a number')
    break
#Will be executed anyhow whether the control goes to try or except
finally:
    print('I will always run at the end.')
'''

'''
Sets
s = {1,2,3}
s.add(4)
'''

'''
In Python JSON is very similar to Dictionary. But JSON could be read by other languages (JavaScript etc) so they are beneficial.

book = {'tom' : {'name' : 'tom', 'address' : '1 green street, NY', 'phone' : 98989988983}}
import json
#To convert into JSON (as strings)
s = json.dumps(book)

#Write them to a file and then use it appropriately.
with open('E:/data/book.txt',w) as book:
	book.write(s)

#To read it in Python
with open('E:'/data/book.txt',r) as book:
	new_book = book.read()
Output will be like '{'tom' : {'name' : 'tom', 'address' : '1 green street, NY', 'phone' : 98989988983}}'

#To read it in Python as a dictionary
new_s = json.loads(new_book)
Output will be like : {'tom' : {'name' : 'tom', 'address' : '1 green street, NY', 'phone' : 98989988983}}
'''



'''
pow(x,y,z)
It works like x^2 mod z
'''


'''
Sort one list based on another
list1 = [2,3,1]
list2 = ['A','B','C']

#This will sort list2 based on list1
xyz = sorted(zip(list1, list2))

'''