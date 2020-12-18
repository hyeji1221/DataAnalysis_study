import re
pattern = r'life'  # 패턴 앞에는 r을 붙여준다
script = 'life'
re.match(pattern, script)   # script에서 pattern을 찾으세요 -> <re.Match object; span=(0, 4), match='life'>
b = re.match(pattern, script).group()  #group()을 이용해 매치된 내용 반환 -> life
# re.match(r'life', 'life').group()과 동일

print(b)
