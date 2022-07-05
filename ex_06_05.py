# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
#Use 'find' and string slicing to extract the portion of the string after the colon character and then use the 'float' function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475  '
locofcolon = str.find(':')
print(locofcolon)
#18
#print(str[locofcolon+1 : ])
# 0.8475  
num = str[locofcolon+1 : ] # 이렇게 뽑은건 여전히 String임을 명심
fin = float(num.strip())
print(fin)
#0.8475
print(type(fin))
#<class 'float'>