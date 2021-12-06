x = "python"
print(type(x))
y = 'python'
print(type(y))
z = """python"""
print(type(z))
print(x[0]) #accessing string elemnts [positive indexing]
print(y[-1]) #accessing string elemnts [negative indexing]
print(x[2:5])  #accessing string elemnts in range [positive indexing]
print(x[-4:-2]) #accessing string elemnts in range [negative indexing]
print(x[:-2])   #accessing string elemnts with only ending range which is exclusive in nature [positive indexing]
                #default start index will be zero always 
print(x[2:])   #accessing string elemnts with only starting range [positive indexing]

abc = """hi
i am sam 
i am from vit"""
print(abc)
print(abc[0])
print(abc[1])
print(abc[2])   # here output will be coming like "\n(this represent as new line)"

xx = "problem solving"
print(xx[1:10:2]) #start,stop,step (positve indexing) and stop is exculive in nature keep in mind bro
print(xx[-10:-2:2]) # start ,stop, step (neagtive indexing) 
print(len(xx))  # we are counting the length size of string using len()

#sting concatenation
d ="Basic"
e = "Electronics"
#from below example we can see the space is also a character 
print(d+e)
print(d+" "+e)

#string repetition 
print(e*5)   # (*) = repetiton [i hope you have read in basic of python if not its ok]

#string method
print(e.lower()) #for converting in lower 
print(e)
print(e.upper())

#replace method 
txt="hello, And Welcome To My World"
x = txt.replace("e","*")
print(x) 
x = txt.replace("ll","**")
print(x)
x = txt.replace("z","1234567890")  # no cahnge of cahrater if character is not in string 
print(x)

#strip method 
s = "python programming"
print(len(s))
print(s.strip())   # strip method removes the space from begin or end BUT not in between 

#rstrip method
print(len(s))
print(s.rstrip())  #rstrip method will remove spcae from right side of the string 

#lstrip method
print(len(s))
print(s.lstrip())  #rstrip method will remove spcae from left side of the string 

#split method 
x = txt.split()  #split() method splits the string in the list format [sting to substring and also use separator]
#default separator is space 
print(x)

# 
x = txt.split("And")
print(x)

#
x = txt.split("o")
print(x)

#max split
x = txt.split("o",1) # max split: list will continue the specified number of elements plus 1
print(x) 

# JOIN method 
y = "GOURAV"
x = ("*".join(y)) #join method combines the string with the given srting 
print(x)

x = ("  ".join(y))
print(x)

# join method in list 
my_tuple = ("ECE","EEE","CSE")
x = ("$".join(my_tuple))
print(x)

"""
my_tuple1 = ("ECE","EEE","CSE",100) #addition of integer will  not work in this case keep in mind
x = ("$".join(my_tuple1))
print(x)
"""

#capaitalize method 
z = "basic electronics"
print(z.capitalize()) #capatalize the first elemnts in the string and give in return


# centre method 
x = "orange"
z = x.center(20)  # centre()bring to middle using the interger you have assigned 
                  # if you will leave empty it will give an error so keep in mind 
y = x.center(20,"*")
print(len(x))
print(z)
print(len(z))
print(y)
print(len(y))



#.count() method
txt = "I love oranges, orange are my favourite fruit."
print(len(txt))
print(txt.count("orange"))  #put the words in ("") you wanna count
                            # using this fuction 
print(txt.count("oranges")) # thses both as diifernt output see closely
print(txt.count("z"))
print(txt.count("o"))
print(txt.count("orange",10,24)) # here 10 and 24 is index for starting and ending point
print(txt.count("my",10,24))

#index
#index() method returns value error,if pattern is not available 
print(txt.index("love"))  
print(txt.index("orange")) # here it will count whole words as one 
                            #returns the index of first occurance 
print(txt.index("orange",10,24))  # here it will count with each and very character of that 
                                  #looks for the pattern between start and end index
#print(txt.index("z"))  this will give you error 
#cause the charater z is not their so it will return the error

#find method (devleoped for same purpose by differnt people)
#find() method returns value -1,if pattern is not available 
print(txt.find("love"))
print(txt.find("orange"))
print(txt.find("orange",10,24))
print(txt.find("z"))

#endswith() method returns true, if strings ends with the speacified value,otheriwse false.
#syntax : string.endswith(value,start,end)
print(txt.endswith("."))
print(txt.endswith("t."))
print(txt.endswith("fruit."))
print(txt.endswith("my"))
print(txt.endswith("oranges",0,13))
#stop index is exclusive and output will be false
print(txt.endswith("oranges",0,14))
#stop index is exclusive and output will be true



#startswith() method
# returns true if the string starts with the specified value,otheriwse false.
#syntax: string.startswith(value,start,end)

print(txt.startswith("I"))
print(txt.startswith("love"))
print(txt.startswith("ora",5,20))
print(txt.startswith("ora",16,20))

#isalnum() method 
#The isalnum() method returns True if all the characters are alphanumeric,
#meaning alphabet letter (a-z) and numbers (0-9) and maybe both.
x = "123"
print(x.isalnum())
x = "SAM"
print(x.isalnum())
x = "123SAM"
print(x.isalnum())
x = "!@#$%"
print(x.isalnum())


#isalpha():The isalpha() method returns True if all the characters are alphabet letters (a-z). 
#Example of characters that are not alphabet letters: (space)!#%&? etc.
x = "SAM"
print(x.isalpha())
x = "123"
print(x.isalpha())
x = "!@#$%"
print(x.isalpha())

#isdigit():The isdigit() method returns True if all the characters are digits, otherwise False. 
#Exponents, like ², are also considered to be a digit.
x = "SAM"
print(x.isdigit())
x = "123"
print(x.isdigit())
x = "!@#$%"
print(x.isdigit())


#islower():In Python, islower() is a built-in method used for string handling. 
#The islower() method returns True if all characters in the string are lowercase, otherwise, returns “False”.
x = "SAM"
print(x.islower())
x = "123"
print(x.islower())
x = "sam is great and i am crazy for him"
print(x.islower())
x = "customer123"
print(x.islower())
x = "Customer123"
print(x.islower())

#isupper():The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
x = "SAM"
print(x.isupper())
x = "123"
print(x.isupper())
x = "sam is great and i am crazy for him"
print(x.isupper())
x = "customer123"
print(x.isupper())
x = "Customer123"
print(x.isupper())
x = "CUSTOMER123"
print(x.isupper())


#in or not in 
x = "python"
y = "pyt" in x
print(y)

x = "python"
y = "pn" in x
print(y)

x = "python"
y = "p" in x
print(y)

#ESCAPE CHARACTER
# Escape Characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert. 
"""x = "i like "python" programming"
print(x)""" # this will give error 

x = "i like 'python'programming "
print(x)

x = "i like \"python\"programming"
print(x)

x = "hello\nworld"  #\n : new line charater  
print(x)

x = "hello\tworld"  #\n : tab space charater  
print(x)

x = "\bombay"  #\b : b is for backspace charater  
print(x)

x = "\\bombay"
print(x)

x = "a\nb\tc"
print(x)

x = "c:\new\code"
print(x)

x = "c:\new\time" 
print(x)

x = "c:\\new\\time"
print(x)

x = r"c:\new\time" #r: raw string (both capital and small works )
print(x)

x = R"c:\new\time" #r: raw string 
print(x)

#carriage return or \r
x = "Problem Solving and Programming CSE100"
print(x)
x = "Problem Solving and Programming \rCSE100"
print(x)
x = "Problem Solving and Programming \rCSE1000"
print(x)


#sorted method 
#unicode

x = ["a","x","c","z","m"]
y = sorted(x)
print(y)

x = ["a","x","c","z","m"]
y = sorted(x,reverse = True)
print(y)

x = ["a","x","c","z","m"]
y = sorted(x,reverse = False)
print(y)

x = [10,100,-2,-3] #desending order 
y = sorted(x,reverse = True)
print(y)

x = [10,100,-2,-3] #assending order
y = sorted(x,reverse = False)
print(y)

#anagram 
raw_s = r'\"'
print(raw_s)

raw_s = r'aa\\'
print(raw_s)

raw_s = R'\\\"'
print(raw_s)

#for loop 
myjob = "teacher"
for k in myjob:
    print(k)

for k in "teacher":
    print(k)

for k in "teacher":
    print(k,end = " ")

#extended slicing 
x = "programming"
print(x[1:10:2])

x = "programming"
print(x[-2:-8:-2])

x = "programming"
print(x[:-8:-2])

#string reversing 
x = "hello"
print(x[-1::-1])


x = "hello"
print(x[::-1])
s
