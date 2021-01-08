# CSV 파일로 데이터 다루기

## CSV 데이터 알아보기

CSV는 쉼표로 나눠진 값을 저장한 데이터를 의미한다

엑셀에서도 활용가능하며 글꼴과 같은 서식 정보가 없기에 조금 더 원형 그대로 가공하기 좋은 데이터 형식이다

## 파이썬으로 CSV 파일 읽고 쓰기

```python
# CSV 파일 불러오는 함수
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output   
```

```python
# CSV형 리스트를 CSV 파일로 저장하는 함수
def writecsv(filename, the_list):
    with open(filenaem, 'w', newline= '') as f:
        a = csv.writer(f, delimiter = ',') # 사용할 CSV형 리스트 원소가 ,(쉼표)로 구분되어 있을 때는 생략 가능
        a.writerows(the_list)
```

## CSV 파일 안의 문자를 숫자로 전환하기

위에서 만든 2개의 함수는 모든 자료를 문자형으로 불러온다

### float() 함수로 바로 바꾸기

자릿수에 쉼표(,)가 있는 경우는 re.sub()함수를 이용해 제거 후 float()함수 사용하기

### 숫자 원소만 골라서 쉼표 제거하기

```python
k = []
for j in i:
    if re.search('\d', j):	# j에 숫자가 들어 있다면
        k.append(float(re.sub(',','',j)))	# 쉼표를 삭제하고 실수형으로 바꿔 k에 저장하기
    else:
        k.append(j)
```

### 문자와 숫자가 섞인 원소 골라내기

'123강남'이라는 원소가 있을 경우 문자열로 인식

```python
for j in p:
    if re.search('[a-z가-힣]', j):	# j에 알파벳 또는 한글이 있따면 그대로 k에 저장
        k.append(j)	
    else:
        k.append(float(re.sub(',','',j)))
```

### 특수문자와 숫자가 섞인 원소 골라내기

!(느낌표)가 포함된 원소는 문자열로 인식

```python
for j in p:
    if re.search('[a-z가-힣!]', j):	# search() 함수에 느낌표(!) 추가
        k.append(j)	
    else:
        k.append(float(re.sub(',','',j)))
```

### 예외 처리로 오류 넘어가기

예를 들어 ''(빈 문자열)을 원소로 집어넣으면(빈 문자열을 숫자형으로 바꿔야하는 경우) 바로 오류가 난다. -> float 함수는 숫자형으로 정확하게 바꿀 수 있는 인수만 받고 나머지는 오류를 일으키기 때문

아래의 코드를 통해 숫자만 골라서 숫자형으로 바꿀 수 있다.

```python
for j in i:  #i는 원소가 들어있는 리스트
    try:
        i[i.index(j)] = float(re.sub(',','',j)) # float형으로 변환 가능하면 변환
    except:
        pass	# float 형으로 변환할 수 없다면 넘어가기
```

## CSV 파일 데이터 분석하기

CSV형 리스트 활용법을 다루는 이유

- 반복문과 조건문을 연습하는데 큰 도움
- 파이썬의 리스트기능 활용 가능

### 번역한 예뮨을 표로 저장하기

1. 영어 원문을 번역한다
2. 각각 Korean, English라는 객체를 만들어 저장한다
3. re.split() 함수를 사용해 마침표(.)로 문장을 구분해 리스트로 저장한다
4. CSV형 리스트를 저장할 빈 리스트 객체를 만든다
5. 여엉 문장 하나, 한국어 문장 하나를 각각 리스트로 만들어서 빈 리스트에 추가한다
6. usecsv 모듈의 writecsv() 함수를 활용해 CSV 파일을 쓴다.



```python
#usecsv 모듈
import csv, os, re

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output


def writecsv(filename, the_list):
    with open(filename, 'w', newline = '')as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

        
def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','', j))
            except:
                pass
            
    return listName
```

