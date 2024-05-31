# ClassroomGradeHelper

A Python script to calculate and analyze student grades across multiple subjects, providing feedback on approval or the need for further study.

## Features
- Input grades for multiple subjects.
- Calculate the average grade for each subject.
- Determine if a student is approved or needs further study (recovery).

## How to Use
1. Run the script.
2. Enter the number of subjects.
3. Enter the school average required for approval.
4. Input the grades for each subject when prompted.
5. View the results including the average grade and status for each subject.

## Example
```python
# Example of input and output
Number of subjects: 3 
School average: 7
------Basic information saved!------
Name of the 1th subject: Math
Grades of Math exams (separated by space): 5 6 7
Name of the 2th subject: Science
Grades of Science exams (separated by space): 8 9 7
Name of the 3th subject: History 
Grades of History exams (separated by space): 6 7 8

# Output
Subject: Math, Average: 6.00, Status: Recovery
Subject: Science, Average: 8.00, Status: Approved
Subject: History, Average: 7.00, Status: Approved
