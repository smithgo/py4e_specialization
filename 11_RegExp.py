# 2022.07.11
# 11. Regual Expressions

# (1) 정규식을 이용한 패턴 찾기 by using re.search()
# smart search라고 생각하면 됨

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.find('From:') >= 0 :
        print('find() 사용:', line)


# Using re.search() like fine()
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From:', line) :
        print('정규식 사용:', line)


# Using re.search() like startswith()
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.startswith('From:') :
        print('startswith() 사용:', line)

import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^From:', line) :
        print('정규식 ^ 사용:', line)


# Wild-Card Characters
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^X.*:', line) :
        print('정규식 ^.* 사용:', line)


# Fine-Tuning Your Match
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^X-\S+:', line) :
        print('정규식 fine-tuning 사용:', line)



# (2) 정규식을 이용한 패턴 추출 by using re.findall()
# re.findall()은 매칭되는 Strings를 추출하는 것, while re.search()는 Boolean으로 값 return
import re
x = 'My 2 favorite numbers are 19 and 50'
y = re.findall('[0-9]+', x)   # [조건] : 괄호 안 조건 만족하는 문자 1개를 의미; 한자리 이상의 숫자
print(y)
#['2', '19', '50']

# 조건을 만족하는 String을 찾지 못하면 빈 리스트 뱉어내
z = re.findall('[AEIOU]+', x) 
print(z)
#[]   # 'M'은 대문자이지만 AEIOU에 해당되지 않아

# re.findall()은 capital-sensitive
q = re.findall('[AEIOU]+', 'AeroEzOlA')
print(q)
#['A', 'E', 'O', 'A']

# War
# ning: Greedy Matching
# 조건을 만족하는 여러 종류의 문자열을 찾은 경우, 긴 쪽을 return
# e.g. re.findall('^F.+:', x)

# Non-Greedy Matching
# e.g. re.findall('^F.+?:', x)


#Fine-Tuning String Extraction
a = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('\S+@\S+', a)   #'\S+'은 최소한 1개 이상의 공백제외 문자
print(b)
#['stephen.marquard@uct.ac.za']

# ()를 사용하면 더 정교한 추출 가능; they tell where to start and stop what string to extract
c = re.findall('^From (\S+@\S+)', a)   # From 다음 괄호가 없었다면 'From~'부터 추출 대상
print(c)
#['stephen.marquard@uct.ac.za']


# Chapter 06. Strings에서 배운 내용으로 이메일 호스트 추출하기
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
#21
sppos = data.find(' ', atpos)
print(sppos)
#31
host = data[atpos+1 : sppos]
print(host)
#uct.ac.za

# The Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
#uct.ac.za

# The Regex Version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
w = re.findall('@([^ ]*)', lin)   # 공백 아닌 문자들이 여럿 나온다 = 빈칸 나올때까지 추출해라
print('w:', w)
#w: ['uct.ac.za']

# Even Coller Regex Version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
r = re.findall('^From .*@([^ ]*)', lin)
print('r:', r)
#r: ['uct.ac.za']

# Exercise. Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :
        continue
    #print(stuff)
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
#Maximum: 0.9907

# Escape Character
import re
pay = 'We just received $10.00 for cookies.'
rt = re.findall('\$[0-9.]+', pay)
print(rt)
#['$10.00']