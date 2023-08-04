import csv

with open('grades.csv', 'w', newline='') as f0:
    w0 = csv.writer(f0)
    w0.writerow(['First Name','Last Name','Grade','Exam 1','Exam 2','Exam 3'])
