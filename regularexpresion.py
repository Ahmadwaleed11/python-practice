import re

pattern="my"
text="hello my name is ahmad waleed"
match=re.search(pattern,text)
print(match)