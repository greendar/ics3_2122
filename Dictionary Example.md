```Python
alphabet = 'abcdefghijklmnopqrstuvwxyz ,?'
alphaD = {}

for letter in alphabet:
    alphaD[letter] = 0
    
text = 'do not forget your phone on the table in the computer science room?'

for letter in text:
    alphaD[letter] += 1

for key in alphaD:
    print(key, alphaD[key])

```
