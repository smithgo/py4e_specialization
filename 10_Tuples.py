# 2022.07.07
# 10. Tuples

# 하루 지났으니 복습을 해보자

# (1) 파일 불러. 엔터 치면 'romeo.txt' 나오도록 해.
fname = input('Enter a file name: ')
if len(fname) < 1 :
    fname = 'romeo.txt'
fhand = open(fname)

# (2) 히스토그램 그려볼까?
dicforcount = dict()
for line in fhand :
    #print(line)
    line = line.rstrip()
    #print(line)
    # 불러온 문자열을 빈칸을 기준으로 나누고 리스트로 바꾸기
    linetolist = line.split()
    #print(linetolist)
    # 리스트의 단어를 하나하나 꺼내 보면서 빈도수를 딕셔너리로 만들자
    for word in linetolist :
        dicforcount[word] = dicforcount.get(word, 0) + 1
    #print(dicforcount)

# (3) 가장 많이 나온 단어가 뭐야? 최고 빈도수 단어 몇번 나왔니?
# 여기에서 튜플 개념 필요해. 딕셔너리에 'items()' mothod를 쓰면 된다는 걸 꼭 기억해
bigkey = None
bigval = None

for key, val in dicforcount.items() :
    if bigval is None or bigval < val :
        bigval = val
        bigkey = key
print('The most word in this file:', bigkey)
print('The frequency of the most word:', bigval)

# Tuples are like Lists
# 리스트는 [대괄호]를 쓰는 반면, 튜플은 (소괄호) 사용

# But, Tuples are IMMUTABLE!
# Tuple은 String처럼 요소를 바꿀 수 없어
# 튜플이 가능한건 index & count 두 가지 뿐이야

# 값 저장하고 값에 접근하기에는 리스트보다 튜플이 효율적이라는 것만 알면 돼
# 임시 변수 저장하기에 튜플이 좋아

# Tuples and Assignment
(x, y) = (2022, 'Smithgo')
print(x)
#2022
print(x, y)
#2022 Smithgo
# 소괄호 생략해도 됨
a, b = 2024, 'Smithgo'
print(a, b)
#2024 Smithgo

# Tuples and Dictionaries
# 딕셔너리에 'items()' method 사용하면 (키, 값) 튜플을 요소로 갖는 리스트 생성
d = dict()
d['a'] = 5
d['b'] = 90
d['c'] = 51
for k, v in d.items() :
    print(k, v)
#a 5
#b 90
#c 51
t = d.items()
print(t)
#dict_items([('a', 5), ('b', 90), ('c', 51)])
# 일종의 3개의 튜플로 이루어진 리스트라 생각하면 돼
# 그러나, 아래처럼 프린트하면 오류나
#print(t[1])
#TypeError: 'dict_items' object is not subscriptable

# Tuples are Comparable
# 비교하려면 튜플 안에 든 요소 개수가 같아야 해
# 맨 왼쪽 요소끼리 하나씩 비교하는데, 0 position 수 같으면 그 다음 수끼리 비교
print((0, 1, 2) < (5, 1, 2))
#True
print((0, 1, 20000) < (5, 3, 4))
#True
print(('a', 'b', 'c') < ('a', 'c', 'b'))
#True
print(('가', '나', '다') < ('가', '다', '나'))
#True
print(('가', 'b', 'c') < ('a', 'c', 'b'))
#False
# 파이썬에서는 영문 다음 한글순이다

# Tuples의 특성을 활용하여 Dcitionary key or value를 기준으로 정렬하기
# key를 기준으로 정렬하기
# 1) 딕셔너리에서 items 메소드를 실행해 튜플로 이루어진 리스트 형태 만들기
# 2) 이 리스트를 sorted 함수로 정렬. 그러면 각각의 튜플의 왼쪽 값, 즉 key를 기준으로 정렬됨.
d = {'b' : 1, 'a' : 10, 'c' : 22}
print(sorted(d.items()))
#[('a', 10), ('b', 1), ('c', 22)]

# 만약 위에 출력값을 key와 value로 한줄씩 보기 좋게 출력하고 싶다면 아래와 같이 코드 작성
for k, v in sorted(d.items()) :
    print(k, v)
#a 10
#b 1
#c 22

# value를 기준으로 정렬하기
# 1) 딕셔너리에서 items 메소드를 실행해 튜플로 이루어진 리스트 형태 만들기
# 2) 이 리스트 내 튜플을 활용해 키와 값을 분리
# 3) 키와 값의 위치를 바꾼 리스트 생성
# 4) 생성된 리스트 정렬
d2 = {'a' : 10, 'b' : 1, 'c' : 22}
tmplst = list()  # 3) 과정을 위한 빈 리스트 생성
for k, v in d2.items() :
    tmplst.append((v, k))  # k와 v 순서 바꿈 & 여기서는 튜플 소괄호 반드시 써줘야 해 
print(tmplst)
#[(10, 'a'), (1, 'b'), (22, 'c')]  # value와 key 위치 바꿨어
print(sorted(tmplst))
#[(1, 'b'), (10, 'a'), (22, 'c')]  # 왼쪽 값 value를 기준으로 오름차순 정렬

# 만약 오름차순 아닌 내림차순 원한다면 sorted 함수에 reverse 옵션을 True로 변경할 것
d3 = {'Smith' : 100, 'Charles' : 200, 'Severance' : 50}
tmpl = list()
for (k, v) in d3.items() :
    tmpl.append((v, k))
print(tmpl)
#[(100, 'Smith'), (200, 'Charles'), (50, 'Severance')]
print(sorted(tmpl, reverse = True))
#[(200, 'Charles'), (100, 'Smith'), (50, 'Severance')]

# 가장 많이 등장한 단어 Top 10 출력하기
# 먼저 단어별 빈도수 나타내는 딕셔너리 만들기
fhand = open('romeo.txt')
dic = {}
for line in fhand :
    line = line.rstrip()
    linetolist = line.split()
    for word in linetolist :
        dic[word] = dic.get(word, 0) + 1
# 딕셔너리 만들었으니까 튜플 활용해서 내림차순 하자
tmplist = []
for (k, v) in dic.items() :
    tmplist.append((v, k)) # 빈도수가 v에 해당하니까 k랑 순서 바꿔
    listsorted = sorted(tmplist, reverse=True)
print(listsorted)
# 결과적으로 [(빈도수, 1등빈도수단어), (빈도수, 2등빈도수단어), ...] 형태로 정렬이 돼

# 빈도수 상위 10개 단어를 출력해 보자
for (v, k) in listsorted[:10] :
    print((k, v))
#('the', 3)
#('is', 3)
#('and', 3)
#('sun', 2)
#('yonder', 1)
#('with', 1)
#('window', 1)
#('what', 1)
#('through', 1)
#('soft', 1)

# List Comprehension (Even Shorter Version) : 지금은 이해 못 해도 문제 없어
# 위의 예시들 중 딕셔너리 d2 사용한 코드를 줄여서 아래와 같이 한방에 쓸 수 있음
# dictionary 특성 중 반드시 기억할 것은 key가 유일하기 때문에 중복된 키는 없어
d2 = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v, k) for k, v in d2.items()]))
#[(1, 'b'), (10, 'a'), (22, 'c')]
# 리스트를 도장처럼 (v. k)로 찍어낸 걸 정렬한 거야