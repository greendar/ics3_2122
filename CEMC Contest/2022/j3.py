# will not work for multi digit numbers
getInput = 'AFB+8HC-4'
lookFor = '+-'
digits = '0123456789'

tempString = ''
for char in getInput:
    if char in digits:
        tempString += char
        print(tempString)
        tempString = ''
    elif char not in lookFor:
        tempString += char
    elif char == '+':
        tempString += ' tighten '
    elif char == '-':
        tempString += ' loosen '


print(tempString)
