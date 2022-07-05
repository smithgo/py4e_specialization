# open()
# The Newline Character: \n
# 개행문자(\n는 하나의 length를 가지는 문자임)

# File Handle as a Sequence
#xfile = open('mbox.txt')
#for cheese in xfile :
#    print(cheese)
# 위를 실행하면 'mbox.txt'파일의 모든 줄이 모두 한줄씩 띄워져 있음

# Counting Lines in a File
fhand = open('mbox.txt')
count = 0
for line in fhand :
    count = count + 1
print('Line Count:', count)
#Line Count: 132045

# Reading the *Whole* File
# 위 방법과 차이점은 모든 줄을 한 줄로 한방에 읽어들이는 것
# e.g. 'mbox.txt'의 132045줄 자료를 1줄로 읽어들임
fhand1 = open('mbox-short.txt')
inp = fhand1.read()
print(len(inp))
#94626
print(inp[:20])
#From stephen.marquar

# Searching Through a File
fhand1 = open('mbox-short.txt')
for line in fhand1 :
    if line.startswith('From:') :
        print(line)
# OOPS! 위 결과 보면 'From:'으로 시작하는 라인들이 한줄씩 빈 줄이 추가되어 있음 for print()

# 이를 바로잡기 위해서는 rstrip()을 추가하면 해결
fhand1 = open('mbox-short.txt')
for line in fhand1 :
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
# 이제 'From:'으로 시작하는 라인들이 아름답게 빈 줄 없이 봅혀져 있음

# Skipping with 'continue'
fhand1 = open('mbox-short.txt')
for line in fhand1 :
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

#Using 'in' to select lines
fhand1 = open('mbox-short.txt')
for line in fhand1 :
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)

# Prompt for File Name
fname = input('Enter the file name: ')
fhand2 = open(fname)
count = 0
for line in fhand2 :
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname) 
# mbox-short.txt 입력하면
#There were 27 subject lines in mbox-short.txt
# mbox.txt 입력하면
#There were 1797 subject lines in mbox.txt

# Bad File Names
# 위 예시에 더해 파일 이름을 적합하지 않게 입력한 경우를 대비한 코드 추가
fname = input('Enter the file name: ')
try :
    fhand2 = open(fname)
except :
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand2 :
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname) 




