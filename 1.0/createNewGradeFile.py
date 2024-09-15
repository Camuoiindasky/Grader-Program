import csv
import os

# Create New File

stp = True
while stp == True:
    step2 = input('Want to create a new file? a/d/n ')
    if step2 == 'y':
        with open('grades.csv', 'w', newline='') as f0:
            w0 = csv.writer(f0)
            w0.writerow(['First Name','Last Name','Grade','Exam 1','Exam 2','Exam 3'])
    elif step2 == 'n':
        print()
        stp = False
