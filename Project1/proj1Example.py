class Character:
  def __init__(self, name, prof, level):
    self.name = name
    self.prof = prof
    self.level = int(level)

  def __str__(self):
    line = "\n\n**************************************\n"
    line += f"Name: {self.name}\n"
    line += f"Class: {self.prof}\n"
    line += f"Level: {self.level}\n"
    line += f"23434545 xp until level {self.level + 1}\n"
    line += "**************************************\n"
    return line

def getChar(listIn):
  nameIn = input("What is the character name?:  ")
  classIn = input("What is the character's profession?:   ")
  levelIn = input("What is the character's level?:    ")
  newChar = Character(nameIn, classIn, levelIn)
  listIn.append(newChar)
  print('\n'*4)

def printMenu():
  print('Please enter what you would like to do:')
  print('1. Enter a New Character')
  print('2. Print Last Character')
  print('3. Exit Program')

#main
charList = []

while True:
  printMenu()
  choice = int(input(":"))
  if choice == 1:
    getChar(charList)
  elif choice == 2:
    print(charList[-1])
  elif choice == 3:
    break
  else:
    print("I don't understand what you picked.", '\n'*3)
