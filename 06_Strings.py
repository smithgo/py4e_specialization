# 2022.07.05
# 06. Strings

## (1) Looping Through Strings
from tempfile import _TemporaryFileWrapper


user_name = 'smithgo'

# while 구문
index = 0
while index < len(user_name) :
    letter = user_name[index]
    print(letter)
    index = index + 1
#s
#m
#i
#t
#h
#g
#o

# for 구문: 훨씬 깔끔
for letter in user_name :
    print(letter)
#s
#m
#i
#t
#h
#g
#o

## (2) Looping and Counting
# e.g. 문자열 안에 특정 글자가 몇 개 있나?
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
#3

## (3) Slicing Strings
myString = 'Smith Go'
print(len(myString))
#8
# 콜론(:) 다음에 오는 두 번째 숫자는 포함하지 않음을 주의
print(myString[0:4])
#Smit
# 문자열 길이 넘어서는 숫자를 입력해도 파이썬이 알아서 끝에서 멈춤
print(myString[4:10])
#h Go
print(myString[:7])
#Smith G
print(myString[3:])
#th Go

## (4) Using 'in' as a Logical Operator
favoritefruit = 'banana'
if 'n' in favoritefruit :
    print('Found it!')
#Found it!

# ※ String Comparison
# String이 모두 대문자 or 소문자로 시작할 때 사용 가능
# 만약 chuck vs. Glen인 경우, Glen이 앞으로 와
myname = 'smithgo'
if myname == 'smithgo' :
    print('All right, smithgo.')
#All right, smithgo.

myname = 'alien' 
if myname < 'smithgo' :
    print('Your name,' + myname + ', comes before smithgo.')
elif myname > 'smithgo' :
    print('Your name,' + myname + ', comes after smithgo.')
else :
    print('All right, smithgo.')
#Your name,alien, comes before smithgo.

myname = 'tailoer' 
if myname < 'smithgo' :
    print('Your name,' + myname + ', comes before smithgo.')
elif myname > 'smithgo' :
    print('Your name,' + myname + ', comes after smithgo.')
else :
    print('All right, smithgo.')
#Your name,tailoer, comes after smithgo.

## (5) String Library; method
greet = 'Hello SmithGo'
print(greet.lower())
#hello smithgo
print(greet.upper())
#HELLO SMITHGO
# method를 사용해도 원래 'greet'은 변하지 않는 것이 중요
print(greet)
#Hello SmithGo
print('Hi THERE'.lower())
#hi there

# 객체지향
print(type(greet))
#<class 'str'>
# 문자열 자료 'greet'에 사용할 method를 모두 보고 싶다면?
print(dir(greet))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 그 외 method
print(greet.find('Go'))
#11
print(greet.find('z'))
#-1
print(greet.replace('Go', 'Kim'))
#Hello SmithKim
print(greet.replace('o', 'XX'))
#HellXX SmithGXX

greet2 = '      Hello SmithGo   '
print(greet2)
#      Hello SmithGo       
print(greet2.lstrip())
#Hello SmithGo   
print(greet2.rstrip())
#      Hello SmithGo
print(greet2.strip())
#Hello SmithGo

#Prefixes: 'greet'이 특정 문자열로 시작하니? (Boolean)
print(greet.startswith('He'))
#True
print(greet.startswith('he'))
#False

## (6) Parsing and Extracting
# e.g. 가상의 이메일 주소 정보에서 이메일 호스트 알아보기
data = 'From your.email.user.name@smith.go.com Tue Jul 5 16:39:56 2022'
atpos = data.find('@')
print(atpos)
#25
locofblank = data.find(' ', atpos)
print(locofblank)
#38
hostname = data[atpos+1 : locofblank]
print(hostname)
#smith.go.com