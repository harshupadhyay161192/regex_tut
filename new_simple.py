import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# 321-555-4321


pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)


sentence = 'Start a sentence and then bring it to an end'

patternn = re.compile(r'sentence')

matches = patternn.search(sentence)

#for match in matches:
print(matches)





