# 실습예제 - 'mbox-short.txt' 자료에서 요일(2 position) 뽑아내기
#fhand = open('mbox-short.txt')
#for line in fhand :
#    line = line.rstrip()
#    words = line.split()
#    if words[0] != 'From' :
#        continue
#    print(words[2])
#Sat
#Traceback (most recent call last):
#  File "/Users/jooingo/Desktop/Learn_Python/PY4E_S/PY4E/08_Lists/ex_08_.py", line 6, in <module>
#    if words[0] != 'From' :
#IndexError: list index out of range

# 위에 보면 'Sat' 찾았는데 그 이후로 에러가 났어.
# 이런 경우는 에러가 난 바로 직전후로 print를 해서 오류 트래킹 해봐
#fhand = open('mbox-short.txt')
#for line in fhand :
#    line = line.rstrip()
#    # 보니까 빈 리스트도 있어. 이것도 프린트 해보자
#    print('Line:', line)
#    words = line.split()
#    print('Words:', words)
#   if words[0] != 'From' :
#        print('IGNORE')
#        continue
#    print(words[2])

# 결국 빈 리스트 때문에 'out of range' 오류가 발생한 거야
# 추가 조치를 아래처럼 2가지 Guardian으로 취해 보자
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    print('Line:', line)
    words = line.split()
    print('Words:', words)
    # 1st possible Guardian
    if len(words) < 1 :
        continue
    if words[0] != 'From' :
        print('IGNORE')
        continue
    print(words[2])

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    print('Line:', line)
    # 2nd possible Guardian
    if line == '' :
        print('Skip Blank')
        continue
    words = line.split()
    print('Words:', words)
    if words[0] != 'From' :
        print('IGNORE')
        continue
    print(words[2])

# 최종 코드는 아래와 같다. (오류 알아보려고 넣었던 print 모두 빼자)
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    words = line.split()
    # Guardian a bit stronger
    if len(words) < 3 :
        continue
    if words[0] != 'From' :
        continue
    print(words[2])

# Gardian과 동일하게 작용하도록 'or' statement 활용 가능
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    words = line.split()
    # Guardian in a compound statement
    if len(words) < 3 or words[0] != 'From' :
        continue
    print(words[2])

# 'or'을 사용할 때 중요한 것은 statement의 순서
# 만약 앞쪽 statment가 참이면 뒤쪽 statement는 확인하지 않음
# 따라서 위 예시에서 'or'의 앞뒤를 바꾸어 주면 오류가 다시 남
# 간단히 생각하면 적합한 순서는 'Guardian pattern' + 'or' + '위험할 수 있는 코드'
