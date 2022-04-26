f = open('textRR.txt', 'r')

digits = '0123456789'
punc = '!@#$%^&*()_+-=[]{},./<>?:;'

for line in f:
    for character in line:
        print(character)

f.close()
