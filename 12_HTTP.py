# 2022.07.12
# 12. HTTP

# Socket은 일종의 전화기라 생각해
# TCP Ports 번호는 어느 서비스로 전화 걸건지 결정하는 거야 like 이메일, 웹페이지 등등

# HyperText Transfer Protocol
# 브라우저가 서버로부터 인터넷을 통해 웹 문서(e.g. HTML, 이미지)를 받는 경우의 규칙
# Getting Data From The Server
# Making a HTTP Request
#Get http://www.dr-chuck.com/page1.htm HTTP/1.0

# (1) 파이썬을 이용해 웹 데이터 읽어오기
# 1) 소켓을 활용하여 웹 데이터 읽어오기
# 소켓 모듈을 불러오자
import socket
#소켓을 만들자
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓을 연결하자: Host는 전화번호고, Port는 내선번호야
mysock.connect(('data.pr4e.org', 80))   #tuple 형태로 줘야 해
# 파이썬의 문자열인 유니코드를 UTF-8로 바꿔서 전송하자
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True :
    data = mysock.recv(512)   # 매번 512개의 문자를 받는다는 의미
    if(len(data)<1) :
        break
    print(data.decode())   # UTF-8에서 파이썬이 읽도록 유니코드로 변환한 것
mysock.close()


# Unicode and UTF-8 in Python
# 파이썬의 문자열은 모두 유니코드
# 파이썬 외부로 데이터 주고 받을 때는 95%가 UTF-8인데 이는 ASCII와 호환 가능

#ASCII
print(ord('H'))
#72
print(ord('e'))
#101
print(ord('\n'))
#10

# 2) 라이브러리 활용하여 웹 데이터 읽어오기
# Making HTTP Easier With urllib
# 이 라이브러리 사용하면 소켓 이용할 필요 없어
# 소켓 사용한 위에 코드 보면 10줄 정도인데 이걸 4줄에 해결해 줘

# Using urllib in Python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')   # url open에서 헤더가 사용됨
for line in fhand :
    print(line.decode().strip())   # 여기에는 헤더가 없는데, 필요하면 따로 불러야 해

# fhand가 핸들처럼 작동하기 때문에 이전 챔터들에서 배웠듯이 파일처럼 다뤄도 돼
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

dic = {}
for line in fhand :
    linetolst = line.decode().split()
    #print(linetolst)
    for word in linetolst :
        dic[word] = dic.get(word, 0) + 1
print(dic)

# Reading Web Pages
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand :
    print(line.decode().strip())


# (2) BeautifulSoup을 이용한 웹데이터 스크래핑(데이터 추출)
# BeautifulSoup도 라이브러리 이름
# 웹페이지에서 일어날 수 있는 다양한 문제들을 해결해 주는 라이브러리
# url 주면 tag를 줘
# urllib와 함께 사용하면 웹 페이지에 존재하는 모든 링크의 url 출력 가능
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()   # 큰 데이터 아니니까 반복문 말고 read()로 한꺼번에 읽어
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))
#http://www.dr-chuck.com/page2.htm


# Exercise. Beautiful Soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import SSL   # 해킹 관점에서 넣은 것으로 궁금하면 구글링 (인증서 에러를 무시하기 위함)
# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT.NONE

url = input('Enter - ')
html - urllib.request.urlopen(url, context = ctx).read()   # ctx를 활용한 건 https 접속하기 위함
html = urllib.request.urlopen(url).read()
# Bueatiful Soup, 이 복잡한 것들 좀 읽어줘
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')   # soup 객체야, 앵커 태그 가져오렴
for tag in tags :
    print(tag.get('href', None))
#http://www.dr-chuck.com/page2.htm

