#!C:\Python34
import re

text = "This is some text -- with Punctuation"
pattern = 'T\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern , re.IGNORECASE)

print("Text	 :" , text )
print("Pattern		:", pattern)
print("Case-sensitive	 :", with_case.findall(text))
print('Case-insensitive:', without_case.findall(text))