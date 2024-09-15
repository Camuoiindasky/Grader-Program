from edit import *
import os
import pandas as pd


print('Choose action')
start = input('New File (N) / Open File (O)\n')

# Option 'New File'
if start == 'N':
    # If there doesn't exist 'Grades' folder, create one
    if os.path.isdir('Grades') == False:
         os.makedirs('Grades')
    
    # Create a table with header
    df = pd.DataFrame(
        {
            'First Name': [], 'Last Name': [], 'Grade': [], 'Exam 1': [], 'Exam 2': [], 'Exam 3': []
        }
    )

    # Print out the request for user's action
    action = True
    while action:
        print('Choose action')
        action = edit(df)

    # Create a default file name.
    i = 1
    source = 'Grades/'
    fileName = f'New-Grades-{i}.csv'
    while os.path.exists(source + fileName):
        i += 1
        fileName = f'New-Grades-{i}.csv'

    # Ask user if user want to save file
    print('Creating', fileName,)
    action = input('Do you want to save file? [Yes]/[No]\n')
    while not (action == 'Yes' or action == 'No'):
        action = input('Please enter your answer [Yes]/[No]: ')
    if action == 'No': 
        print('Exit program.')
        exit()

    # Ask user if user want to change file name
    action = input('Do you want to change file name? [Yes]/[No]\n')
    while not (action == 'Yes' or action == 'No'):
        action = input('Please enter your answer [Yes]/[No]: ')
    if action == 'Yes':
        fileName = input('Your new file name: ') + '.csv'
        
    # Output the csv file
    df.to_csv(os.path.join(source + fileName), index = False)
    if os.path.exists(source + fileName):
        print(fileName, 'saved successfully.')

# Option 'Open File'
elif start == 'O':
    # List all csv file
    print('Showing existed file.')
    for fileName in os.listdir('Grades'):
        if fileName.endswith('.csv'):
            print(fileName)
    
    # Ask which file user want to open 
    print()
    source = 'Grades/'
    fileName = input('Open file: ') + '.csv'

    # Opend cvs file
    df = pd.read_csv(source + fileName)

    # Print out the request for user's action
    action = True
    cnt = 0
    while action:
        print('Choose action')
        action = edit(df)
        cnt += 1
    
    # Ask user if user want to save file
    print('Updating', fileName,)
    if cnt > 1:
        action = input('Do you want to save file? [Yes]/[No]\n')
        while not (action == 'Yes' or action == 'No'):
            action = input('Please enter your answer [Yes]/[No]: ')
    if action == 'No': 
        print('Exit program.')
        exit()

    # Update the csv file
    df.to_csv(source + fileName, index = False)