def clean(charIn):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    charOut = charIn.upper()
    if charOut in alpha:
        return charOut
    elif charOut == '-':
        return " "
    else:
        return ""

fString = ''
f = open('textRR.txt', 'r', encoding="utf-8")

for line in f:
    for char in line:
        char = clean(char)
        fString += char

f.close()

print(fString)
