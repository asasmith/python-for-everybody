import re
print('hello python for everyone')

str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

whatisthis = re.findall('\S+?@\S+', str)

print(whatisthis)
