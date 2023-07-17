import re
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batma and Tina Fey')
print(mo1.group()) #'Batman'
print(mo1.groups()) #()
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group()) #'Tina Fey'





