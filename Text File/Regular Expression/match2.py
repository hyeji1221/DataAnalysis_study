import re

pattern = r'is'
script = 'life is so cool'

def refinder(pattern, script):
    if re.match(pattern, script):
        print("Match!")
    else:
        print('Not a match!')

refinder(pattern, script)

# 결과 값은 not a match
# match는 텍스트 중간에 있는 패턴을 찾지 못한다
