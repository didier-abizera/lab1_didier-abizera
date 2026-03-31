import csv
import sys
import os

def load_csv_data():
    # Ask the user for the filename
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        # Check if the file is empty
        if len(assignments) == 0:
            print("Error: The file is empty. Please add grades first.")
            sys.exit(1)
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")
    
    # a) Check if all scores are between 0 and 100
    for record in data:
        if not (0 <= record['score'] <= 100):
            print(f"Error: Invalid score {record['score']} for '{record['assignment']}'.")
            sys.exit(1)
    print("All scores are valid.")
    
    # b) Validate total weights
    total_weight = sum(record['weight'] for record in data)
    formative_weight = sum(record['weight'] for record in data if record['group'] == 'Formative')
    summative_weight = sum(record['weight'] for record in data if record['group'] == 'Summative')
    if total_weight != 100:
        print(f"Error: Total weights must equal 100. Got {total_weight}.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weights must equal 60. Got {formative_weight}.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weights must equal 40. Got {summative_weight}.")
        sys.exit(1)
    print("All weights are valid.")
    
    # c) Calculate the final grade and GPA
    formative_grade = sum(record['score'] * record['weight'] for record in data if record['group'] == 'Formative') / formative_weight
    summative_grade = sum(record['score'] * record['weight'] for record in data if record['group'] == 'Summative') / summative_weight
    total_grade = (formative_grade * formative_weight + summative_grade * summative_weight) / 100
    gpa = (total_grade / 100) * 5.0
    print(f"Formative Score: {formative_grade:.2f}%")
    print(f"Summative Score: {summative_grade:.2f}%")
    print(f"Total Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    
    # d) Determine Pass/Fail status
    if formative_grade >= 50 and summative_grade >= 50:
        status = "PASSED"
    else:
        status = "FAILED"
    print(f"\nFinal Status: {status}")
    
    # e) Find failed formative assignments eligible for resubmission
    failed_formatives = [record for record in data if record['group'] == 'Formative' and record['score'] < 50]
    if failed_formatives:
        highest_weight = failed_formatives[0]['weight']
        for record in failed_formatives:
            if record['weight'] > highest_weight:
                highest_weight = record['weight']
        resubmit = [record for record in failed_formatives if record['weight'] == highest_weight]
        print("\nEligible for Resubmission:")
        for record in resubmit:
            print(f"  - {record['assignment']} (Score: {record['score']}%, Weight: {record['weight']})")
    else:
        print("\nNo assignments eligible for resubmission.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
