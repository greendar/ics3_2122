def menu():
    global notDone
    string = '\n\nWhat would you like to choose?\n'
    string += '1. Enter new students.\n'
    string += '2. Print out last student.\n'
    string += '3. Print out all students.\n'
    string += '0. Exit the program.\n'
    print(string)
    choice = input('Enter 0, 1, 2, 3\n: ')
    if choice == '1':
        enterStudents()
    elif choice == '2':
        printLastStudent()
    elif choice == '3':
        printAllStudents()
    elif choice == '0':
        notDone = False
 
def studentLine(file, studentName, studentGrade):
    file.write(studentName)
    file.write('$')
    file.write(studentGrade)
    file.write('\n')
    
def enterStudents():
    f = open(fileName, 'a')
    print(f'{fileName} opened.\nBegin entering students.\n')
    while True:
        print('\n'*3, '*'*30)
        name = input('Enter Name\n: ')
        grade = input('Enter Grade\n: ')
        studentLine(f, name, grade)
        print('*'*30, '\n'*3)
        proceed = input('Would you like to enter another student? (y/n)\n: ')
        if proceed == 'n':
            f.close()
            break
        else:
            print('Next Student', '\n'*3)
        


def printLastStudent():
    pass

def printAllStudents():
    print('\n'*3, 'Student List with Grade', sep='')
    f = open(fileName, 'r')
    for line in f:
        sList = line.split('$')
        print(sList[0], sList[1], end='')
    f.close()

notDone = True
fileName = 'studentDatabase.txt'

while notDone:
    menu()

