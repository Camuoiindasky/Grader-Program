# Hong Ngoc Dinh
# CS1314.010

import csv

"""
with open('grades.csv', 'w', newline='') as f0:
    w0 = csv.writer(f0)
    w0.writerow(['First Name','Last Name','Grade','Exam 1','Exam 2','Exam 3'])
"""
  
# Read grades from a file, list them on the screen.

with open('grades.csv', 'r') as f1:
    f1 = f1.readlines()
    for data in f1:
        (fname, lname, grade, exam1, exam2, exam3) = data.strip().split(',')
        print(fname.ljust(10), lname.ljust(10), grade.ljust(10), exam1.ljust(10), exam2.ljust(10), exam3.ljust(10))

# Search students by name.

with open('grades.csv', 'r') as f2:
    step1 = input('Want to search student name? y/n ')
    if step1 == 'y':
        search = input("Student's Name: ")
        search = search.capitalize()
        f2 = f2.readlines()
        Found = True
        for line in f2:
            if search in line:
                (fname, lname, grade, exam1, exam2, exam3) = line.split(',')
                print(fname.ljust(10), lname.ljust(10), grade.ljust(10), exam1.ljust(10), exam2.ljust(10), exam3.ljust(10))
                Found = True
                break
            else: Found = False
        if Found == False:
            print('There are no stundent named', search)
    else: print()

# Add or delete a student
# Add grades and auto-calculate the average grades of a student.

stp = True
while stp == True:
    step2 = input('Want to add or delete a student? a/d/n ')
    if step2 == 'a':
        with open('grades.csv', 'a', newline='') as f4:
            w1 = csv.writer(f4)
            fname = input('First name: ')
            fname = fname.capitalize()
            lname = input('Last name: ')
            lname = lname.capitalize()
            exam1 = input('Exam 1 score: ')
            exam2 = input('Exam 2 score: ')
            exam3 = input('Exam 3 score: ')
            s = float(exam1) + float(exam2) + float(exam3)
            q = s/3
            if q >= 90: grade = 'A'
            elif q < 90 and q >= 80: grade = 'B'
            elif q < 80 and q >= 70: grade = 'C'
            elif q < 70 and q >= 60: grade = 'D'
            else: grade = 'F'
            w1.writerow([fname,lname,grade, exam1, exam2, exam3])
            print(grade)
    elif step2 == 'd':
        with open('grades.csv', 'a') as f4:
            r1 = csv.writer(f4)
            dname = input("Student's name: ")
            dname = fname.capitalize()
            lst1 = []
            Found = False
            for row in r1:
                if dname in row:
                    Found = True
                else: lst1.append(row)
            if Found == False: print('Student Not Found')
            else:
                with open('grades.csv', 'w',newline='') as f5:
                    w2 = csv.writer(f5)
                    w2.writerows(lst1)
    elif step2 == 'n':
        print()
        stp = False

# Save changes to the file.





