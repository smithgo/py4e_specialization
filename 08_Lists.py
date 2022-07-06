# 2022.07.06
# 08. Lists

# What is not a 'Collection'? >>> variable: 새 값을 넣으면 이전 값에 덮어씌워짐
# List는 컬렉션의 일종으로, 하나의 변수에 여러가지 값을 넣어둔 것

# List 안에 작은 List를 넣어둘 수 있음

# List is Mutable, while String is NOT!
# Strings are not mutable
#fruit = 'Banana'
#fruit[0] = 'b'
#TypeError: 'str' object does not support item assignment
#String의 대소문자 바꾸기는 method 활용할 것

#Lists are mutable
lotto = [2, 14, 26, 41, 63]
print(lotto)
#[2, 14, 26, 41, 63]
print(lotto[2])
#26
lotto[2] = 100
print(lotto)
#[2, 14, 100, 41, 63]

# Using the 'range' function
print(range(4))
#[0, 1, 2, 3] == range(0, 4)
friends = ['charles', 'severance', 'smith']
print(len(friends))
#3
print(range(len(friends)))
#[0, 1, 2] == range(0, 3)

# 아래 (1) 루프와 (2) 루프를 비교해 보자
# (1) 루프
friends = ['charles', 'severance', 'smith']
for friend in friends :
    print('Happy New Year:', friend)
#Happy New Year: charles
#Happy New Year: severance
#Happy New Year: smith

# (2) 루프
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend)
#Happy New Year: charles
#Happy New Year: severance
#Happy New Year: smith

# Lists는 '+'연산자를 활용해 리스트끼리 합칠 수 있지만 '-' 연산자는 ERROR
friends = ['charles', 'severance', 'smith']
alp = ['a']
c = friends + alp
print(c)
#['charles', 'severance', 'smith', 'a']
#print(c-alp)
#TypeError: unsupported operand type(s) for -: 'list' and 'list'

# Is Something in a List?
friends = ['charles', 'severance', 'smith']
print('smith' in friends)
#True
print('a' not in friends)
#True
print('a' in friends)
#False

# 아래 동일하게 평균을 구하는 <1> while 루프와 <2> while 루프를 비교해 보자
# <1> while 루프: 이전 단원에서 배운 방식대로 만들기 (모두 숫자 입력했다 가정)
sum = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    sum = sum + value
    count = count + 1
average = sum/count
print('Average:', average)

# <2> while 루프: 빈 리스트 만들어 붙이는 방법 (모두 숫자 입력했다 가정)
# 더 많은 메모리 잡아 먹음
#numlist = list()
#while True :
#    inp = input('Enter a number: ')
#    if inp == 'done':
#        break
#    value = float(inp)
#    numlist.append(value)
#average = sum(numlist) / len(numlist)
#print('Average:', average)

# Best Friends: Strings and Lists
# 'split()' 활용하면 기본적으로 빈칸을 기준으로 String을 끊어서 단어별 요소로 구성된 List 생성
# String이 단어 간 빈칸이 많더라도, 'split()'은 전부 없애고 단어별로 끊어줌
line = 'A lot         of spaces'
etc = line.split()
print(etc)
#['A', 'lot', 'of', 'spaces']

# 디폴트는 빈칸을 기준으로 문자열을 리스트로 나누지만, 다른 구획문자(delimiter)을 기준으로 바꿀 수 있음
line2 = 'first;second;third'
thing = line2.split()
print(thing)
#['first;second;third']
print(len(thing))
#1

thing2 = line2.split(';')
print(thing2)
#['first', 'second', 'third']
print(len(thing2))
#3