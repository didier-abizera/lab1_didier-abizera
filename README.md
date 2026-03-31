# Lab1_didier-abizera

## Grade Evaluator & Archiver

A Python application that evaluates a student's final academic standing based on a CSV file of course grades, and a Bash script that archives the CSV file.

## Project Structure

- grade-evaluator.py - Python script that evaluates grades
- organizer.sh - Bash script that archives the CSV file
- grades.csv - CSV file containing the grades
- README.md - This file

## How to Run the Python Script

1. Make sure you have Python 3 installed
2. Make sure grades.csv is in the same directory
3. Run the following command:

python3 grade-evaluator.py

4. When prompted, type the filename:

grades.csv

5. The program will display:
- Grade validation results
- Weight validation results
- Formative and Summative scores
- GPA
- Final status (PASSED or FAILED)
- Assignments eligible for resubmission

## How to Run the Shell Script

1. Make sure organizer.sh is executable by running:
chmod +x organizer.sh
2. Run the following command:

./organizer.sh

3. The script will:
- Create an archive folder if it does not exist
- Move grades.csv to the archive folder with a timestamp
- Create a new empty grades.csv
- Log the operation to organizer.log

