# 2022.07.06
# 09. Dictionaries

# Lists vs. Dictionaries
# List는 요소의 순서가 중요하지만, Dictionary는 순서가 없다. 대신 키가 있다.
# 리스트: 순서대로 잘 쌓여진 프링글스
# 딕셔너리: 지갑, 열쇠, 아이패드, 메이크업 도구 등을 몽땅 넣어둔 가방
# 따라서 딕셔너리는 Assiciative Arrays: 키와 값 사이의 연결관계

# List & Dictionary : 빈 리스트/딕셔너리에 요소를 추가하고 변경하는 것도 가능

# Counting Pattern: 히스토그램 그리기
counts = dict()
names = ['서영은', '히카루', '서영은', '박한별', '이효리']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
#{'서영은': 2, '히카루': 1, '박한별': 1, '이효리': 1}

# The 'get' method for dictionaries
# 아래 나오는 4줄 코드가 'get' method를 통해 1줄로 끝낼 수 있어
if name in counts:
    x = counts[name]
else :
    x = 0

# 위는 4줄 코드는 아래 1줄 코드와 동일
x = counts.get(name, 0)

# Simplified counting with 'get()'
counts = dict()
names = ['서영은', '히카루', '서영은', '박한별', '이효리']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
#{'서영은': 2, '히카루': 1, '박한별': 1, '이효리': 1}

# 한줄 안에 있는 단어 수 셀 때
# 일반적으로 split으로 나눈 리스트를 루프에 넣고,
# Dictionary 활용하여 단어별로 수를 추적
counts = dict()
print('Enter a line of text:')
inpline = input('')

inplinetolist = inpline.split()

print('Words in List:', inplinetolist)

print('Counting...')
for line in inplinetolist :
    counts[line] = counts.get(line, 0) + 1
print('Counts:', counts)

# Definite Loop & Dictionary
scorebyst = {'Ast' : 1, 'Bst' : 42, 'Cst' : 100}
for stname in scorebyst :
    print(stname, scorebyst[stname])
#Ast 1
#Bst 42
#Cst 100

# 딕셔너리 key와 value 목록 검색
scorebyst = {'Ast' : 1, 'Bst' : 42, 'Cst' : 100}
print(list(scorebyst))
#['Ast', 'Bst', 'Cst']
print(scorebyst.keys())
#dict_keys(['Ast', 'Bst', 'Cst'])
print(scorebyst.values())
#dict_values([1, 42, 100])
print(scorebyst.items())
#dict_items([('Ast', 1), ('Bst', 42), ('Cst', 100)]) >>> Tuple! coming soon...
# 위 결과 해석: Tuple이라는 자료 구조 안에 딕셔너리의 (key, value) 쌍이 저장된 리스트 
# 'items'를 썼다는 건 곧 변수 2개가 있다는 거야

# 보너스: 두 개의 반복 변수!
# '두 개'의 반복 변수를 사용하여 딕셔너리의 '키-값' 쌍을 반복해서 다룸
# 매번 반복할 때, 첫 번째 변수를 키로, 두 번째 변수는 값에 대응하는 값을 나타냄
scorebyst = {'Ast' : 1, 'Bst' : 42, 'Cst' : 100}
for aa, bb in scorebyst.items() :
    print(aa, bb)
#Ast 1
#Bst 42
#Cst 100
# 이 위에 결과는 aa에 각 학생이름이, bb에 각 학생의 점수가 들어간 것 

# 두 개의 루프를 중첩하여 사용해서 'txt' 파일의 최대 빈도 단어를 구해 보자
fname = input('Enter file: ')   #'words.txt' 입력
fhand = open(fname)

counts = dict()
for line in fhand :
    linetolist = line.split()
    for word in linetolist :
        counts[word] = counts.get(word, 0) + 1
print(counts)
# 이 위까지가 단어별 빈도수를 딕셔너리로 만든 것이고,
# 이제 이 딕셔너리를 활용해서 최대 빈도수 단어를 찾는 거야
bigvalue = None
bigkey = None
for key, value in counts.items() :
    if bigvalue is None or value > bigvalue :
        bigvalue = value
        bigkey = key
print(bigkey, bigvalue)
#to 16

# 복습: 위에 코드 보지 않고 혼자 코드 짜보기
fname = input('Enter a file name: ') #clown.txt
fhand = open(fname)
# 딕셔너리 형태로 각 단어를 key, 단어별 빈도수는 value로 나타내기
dicforcounts = {}
for line in fhand :
    linetolist = line.split()
    for word in linetolist :
        dicforcounts[word] = dicforcounts.get(word, 0) + 1
# 위에서 생성한 딕셔너리 내 최고 빈도수 찾기
bigkey = None
bigvalue = None
for key, value in dicforcounts.items() :
    if bigvalue is None or bigvalue < value :
        bigvalue = value
        bigkey = key
print(bigkey, bigvalue)
#the 7