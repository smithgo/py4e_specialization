# 2022.07.05
# 05. Loops and Iterations

# Loop Idioms
## (1) 최댓값 찾기
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
#Before -1
#9 9
#41 41
#41 12
#41 3
#74 74
#74 15
#After 74

# 파이썬이 훌륭하지만, R과 비교했을 때 아쉬운 점 발견
# 연산자를 '='이 아니라 '->/<-'처럼 화살표 방향으로 했더라면 좋았을 것
# 무조건 '='는 '<-'로 생각하자 
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        the_num = largest_so_far
    print(largest_so_far, the_num)
print('After', largest_so_far)
#Before -1
#-1 -1
#-1 -1
#-1 -1
#-1 -1
#-1 -1
#-1 -1
#After -1

## (2) 리스트의 원소 개수 세기
nork = 0
print('Before', nork)
for thing in [9,41,12,3,74,15] :
    nork = nork + 1
    print(nork, thing)
print('After', nork)
#Before 0
#1 9
#2 41
#3 12
#4 3
#5 74
#6 15
#After 6

## (3) 리스트의 원소 합계 구하기
sork = 0
print('Before', sork)
for thing in [9,41,12,3,74,15] :
    sork = sork + thing
    print(sork, thing)
print('After', sork)
#Before 0
#9 9
#50 41
#62 12
#65 3
#139 74
#154 15
#After 154

## (3) 리스트의 원소 평균 구하기
#원소 개수와 총합을 동시에 활용하면 평균 구하기 가능
count = 0
sum = 0
print('Before', count, sum)
for thing in [9,41,12,3,74,15] :
    count = count +1
    sum = sum + thing
    print(count, sum, thing)
print('After', count, sum, sum/count)
#Before 0 0
#1 9 9
#2 50 41
#3 62 12
#4 65 3
#5 139 74
#6 154 15
#After 6 154 25.666666666666668

## (4) 필터링 (e.g. 특정 값보다 큰 수 print하여 확인)
print('Before')
numbers = [9,41,12,3,74,15]
for thing in numbers :
    if thing > 20:
        print('Large Number', thing)
print('After')
#Before
#Large Number 41
#Large Number 74
#After

## (5) Boolean 활용하여 특정값 있는지 검색
found = False
print('Before', found)
numbers = [9,41,12,3,74,15]
for thing in numbers :
    if thing == 3 :
        found = True
        print(found, thing)
        break # 찾으려던 특정값을 찾았다면 종료하는 것이 적절
print('After')
#Before False
#True 3
#After

## (5) 최솟값 찾기 
#최솟값 찾는 데는 None 자료형, "is (not)" 연산자 활용 필요
#"is" 연산자는 "=" 연산자보다 더욱 강력함
#e.g. 0 == 0.0 (True) vs. 0 is 0.0(False)
smallest = None
print('Before')
numbers = [9,41,12,3,74,15]
for thing in numbers :
    if smallest is None :
        smallest = thing
    elif smallest > thing :
        smallest = thing
    print(smallest, thing)
print('After', smallest)
#Before
#9 9
#9 41
#9 12
#3 3
#3 74
#3 15
#After 3