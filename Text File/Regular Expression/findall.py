import re
number = 'My number is 511223-1****** and yours is 521012-2******'
a = re.findall('\d{6}', number)
print(a)

# ly로 끝나는 단어 추출
sentence = 'I have a lovely dog, really. I am not telling a lie'
b = re.findall(r'\w+ly', sentence)
print(b)

