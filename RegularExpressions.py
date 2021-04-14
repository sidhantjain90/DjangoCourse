import re

patterns = ['term1','term2']

text = 'This is a string with term1, not the other!!'

for pattern in patterns:
    print("I am searching for: "+pattern)

    if re.search(pattern, text):
        print("Match!")
    else:
        print("No Match!")

#Search
match = re.search('term1',text)
print(type(match))

print(match.start())

#Split
split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term, email))



#Findall
print(re.findall('match','test phrase match in match middle'))

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['s[sd]+']

multi_re_find(test_patterns, test_phrase)

## Several options...
#sd*
#sd+
#sd?
#sd{1,3}
#s[sd]+

# Look for symbols
test_phrase1 = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns1 = ['[^!.?]+']

multi_re_find(test_patterns1, test_phrase1)

# Look for lowercase letters
test_patterns2 = ['[a-z]+']

multi_re_find(test_patterns2, test_phrase1)

# Look for digits
test_phrase3 = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns3 = [r'\d+']

multi_re_find(test_patterns3, test_phrase3)
