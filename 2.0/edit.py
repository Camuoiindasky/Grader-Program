def edit(df):
    # List all actions can be choosen
    edit = input("Add new student [A]   Delete student [D]   Search student's name [S]   Show grades [G]   Exit Program[E]\n")
    if edit == 'A': add(df)
    elif edit == 'D': delete(df)
    elif edit == 'S': search(df)
    elif edit == 'G': read(df)
    elif edit == 'E': return False
    else: print('Please choose action.')
    return True

def read(df):
    print(df)

def search(df):
    studentName = input('Enter student name: ')
    studentName = studentName.capitalize()
    if studentName in df['First Name'].values:
        print(df.loc[df['First Name'] == studentName])
    elif studentName in df['Last Name'].values:
        print(df.loc[df['Last Name'] == studentName])
    else: print('No Student')
    

def add(df):
    fName = input('First Name: ')
    fName = fName.capitalize()
    lName = input('Last Name: ')
    lName = lName.capitalize()
    exam1 = float(input('Exam 1 score: '))
    exam2 = float(input('Exam 2 score: '))
    exam3 = float(input('Exam 3 score: '))
    grade = cal(exam1, exam2, exam3)
    df.loc[len(df.index)] = [fName, lName, grade, exam1, exam2, exam3]
    print()
    
def cal(exam1, exam2, exam3):
    q = (exam1 + exam2 + exam3) / 3
    if q >= 90: grade = 'A'
    elif q < 90 and q >= 80: grade = 'B'
    elif q < 80 and q >= 70: grade = 'C'
    elif q < 70 and q >= 60: grade = 'D'
    else: grade = 'F'
    return grade

def delete(df):
    studentName = input('Enter student name: ')
    studentName = studentName.capitalize()
    if studentName in df['First Name'].values:
        df.drop(df[df['First Name'] == studentName].index, inplace = True)
    elif studentName in df['Last Name'].values:
        df.drop(df[df['Last Name'] == studentName].index, inplace = True)
    else: print('No Student')