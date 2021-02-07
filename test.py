import re

a = 'the.simpsons.s03e01.mkv'
sname = re.search(r".+(?=.[sS][0-9]+[eE][0-9]+)", a)
print(sname)
print(sname.group(0))
print(sname.group(0).title())
