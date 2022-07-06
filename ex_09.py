fname = input('Enter a file name: ')
# 추가 입력 없이 enter만 눌러도 특정 파일 넣고 싶다면?
if len(fname) < 1 :
    fname = 'clown.txt'
fhand = open(fname)
# 파일 읽자
dicforcount = {}
for line in fhand:
    line = line.rstrip()
    # print(line)
    linetolist = line.split()
    # print(linetolist)
    for word in linetolist :
        #print(word)
        #print('**', word, dicforcount.get(word, -99)) # 처음 보는 word 나오면 무조건 -99 출력됨
        #oldcount = dicforcount.get(word, 0)  # if the key is not there, the count is zero
        #print(word, 'old', oldcount)
        #newcount = dicforcount.get(word, 0) + 1
        #print(word, 'new', newcount)
        
        # idiom: retrieve/create/update counter

        #if word in dicforcount :
        #    dicforcount[word] = dicforcount[word] + 1
            #print('**Existing**')
        
        #else :
        #    dicforcount[word] = 1
            #print('**New**')
        dicforcount[word] = dicforcount.get(word, 0) + 1
        #print(word, dicforcount[word])
#print(dicforcount)       
        
# Now, we want to find the most common word.
bigkey = None
bigvalue = None

for key,value in dicforcount.items() :
    if bigvalue is None or bigvalue < value :
        bigvalue = value
        bigkey = key  # capture/remember the key that was lasrgest 
print('Done!', bigkey, bigvalue)

    
