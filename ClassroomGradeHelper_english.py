import numpy as np
import webbrowser
from time import sleep

num_subjects = int(input('Number of subjects: '))
school_average = float(input('School average: '))
print('\033[33m-------Basic information saved!------\033[0m')
sleep(0.4)

subjects = []

for i in range(num_subjects):
    subject = str(input(f'Name of the {i+1}th subject: '))
    grades = str(input(f'Grades of {subject} exams (separated by space): ')).split()
    print('\033[33m---------Subject/Grades saved!--------\033[0m')
    sleep(0.4)
    grades = [float(grade) for grade in grades]
    subjects.append([subject] + grades)

print('\033[33m-------------Processing...------------\033[0m')
sleep(0.7)

for subject in subjects:
    name = subject[0]
    grades = np.array(subject[1:])
    average = np.mean(grades)
    status = '\033[32mApproved\033[0m' if average >= school_average else '\033[31mRecovery\033[0m'
    print(f'\033[1;33mSubject:\033[0m {name:25} \033[1;33mAverage:\033[0m {average:.2f} \033[1;33mStatus:\033[0m {status}')

sleep(1.5)
print('\033[35mCreated by: VitorRenanSD\033[0m')
webbrowser.open('https://github.com/VitorRenanSD')
