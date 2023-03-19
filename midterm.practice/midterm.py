# SAMPLE OUTPUT:
#
# Student Information
# Name: Jon Snow
# Student Number: 33415221
# ----------------------
# Course Information
# Course Title: Intro to Python
# Course Code: CST8279
# ----------------------
# Mark Breakdown
# Assignments: 25/40
# Midterm: 25/35
# Exam: 25/25
#
# Percent Grade: 75%
# Letter Grade: B


# 5 marks
# Prompt the user for inputs
# Validate the inputs
# Student number is exactly 8 digits
# Function returns a string and int value (Name and Student#)
def get_student_info():
    name = input("Please enter your name: ")
    student_number = input("Please enter your student number: ")

    while True:
        if len(student_number) != 8 or not student_number.isdigit():
            student_number = input("Invalid input. Please enter your 7-digit student number: ")
        else:
            break

    return name, input(student_number)


# 5 marks
# Prompt the user for inputs
# Validate the inputs
# Course code is exactly 7 characters
# Function returns two string values (Course Title and Course Code)
def get_course_info():
    course_title = input("Please enter the course title: ")
    course_code = input("Please enter the course code: ")

    while True:
        if len(course_code) != 7:
            course_code = input("Invalid input. Course code must be exactly 7 characters long: ")
        else:
            break

    return course_title, course_code


# 5 marks
# Prompts the user for the weights of each component: Assignments, Midterm, Exam
# Validate the inputs
# Weight value for each component is between 0 and 100.
# Function returns 3 float values. wAssignment, wMidterm, wExam
def get_assessment_weights():
    w_assignment = input("Please enter the weight for assignments: ")
    w_midterm = input("Please enter the weight for the midterm: ")
    w_exam = input("Please enter the weight for the exam: ")

    while True:
        try:
            w_assignment = float(w_assignment)
            w_midterm = float(w_midterm)
            w_exam = float(w_exam)

            if w_assignment < 0 or w_assignment > 100 or w_midterm < 0 or w_midterm > 100 or w_exam < 0 or w_exam > 100:
                raise ValueError("Invalid input. Weight value must be between 0 and 100.")
            break

        except ValueError as e:
            print(e)
            w_assignment = input("Please enter the weight for assignments: ")
            w_midterm = input("Please enter the weight for the midterm: ")
            w_exam = input("Please enter the weight for the exam: ")

    return w_assignment, w_midterm, w_exam


# 5 marks
# Returns True if the sum of the 3 arguments is 100. False otherwise
# Assign the default values 40, 35, 25 to wAssign, wMidterm and wExam respectively
def check_weights(wAssign=40, wMidterm=35, wExam=25):
    weight_sum = wAssign + wMidterm + wExam

    if weight_sum == 100:
        return True
    else:
        return False


# 5 marks
# Prompts the user for the number of assignments
# Validate the inputs
# Keep prompting until the number is a positive integer.
# Returns the number of assignments
def get_number_of_assignments():
    num_assignments = input("Please enter the number of assignments: ")
    while True:
        try:
            num_assignments = int(num_assignments)

            if num_assignments <= 0:
                raise ValueError
            break

        except ValueError:
            num_assignments = input("Value error! Please enter a positive integer for the number of assignments: ")

    return num_assignments


# 5 marks
# Convert the percent grade to a letter grade according to the conversion table
# in the course outline
def calculate_alpha_grade(percent_grade):
    if percent_grade >= 90:
        return "A+"
    elif percent_grade >= 85:
        return "A"
    elif percent_grade >= 80:
        return "A-"
    elif percent_grade >= 77:
        return "B+"
    elif percent_grade >= 73:
        return "B"
    elif percent_grade >= 70:
        return "B-"
    elif percent_grade >= 67:
        return "C+"
    elif percent_grade >= 63:
        return "C"
    elif percent_grade >= 60:
        return "C-"
    elif percent_grade >= 57:
        return "D+"
    elif percent_grade >= 53:
        return "D"
    elif percent_grade >= 50:
        return "D-"
    else:
        return "F"

    return calculate_alpha_grade()


# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------

# 5 marks
# Get the weight values of each assessment component (call the appropriate function)
# Check if summation of weight values is 100 (call the appropriate function)
# If False, repeat until True.

#while True:
#   w_assignment, w_midterm, w_exam = get_assessment_weights()
#   if check_weights(w_assignment, w_midterm, w_exam):
#      break
#  else:


# 10 marks
# Get the number of assignments
# For each assignment prompt the user to enter assignment grades
# Validate the input as a float between 0 and 100
# Calculate the average assignment grade.

def get_average_assignment_grade():

    num_assignments = get_number_of_assignments()
    sum_assignment_grades = 0

    for i in range(num_assignments):
        while True:
            try:
                assignment_grade = float(input(f"Enter the grade for assignment {i+1}: "))
                if assignment_grade < 0 or assignment_grade > 100:
                    raise ValueError("Grade must be between 0 and 100")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
        sum_assignment_grades += assignment_grade
    average_assignment_grade = sum_assignment_grades / num_assignments

    return average_assignment_grade


# 5 marks
# Prompt the user to enter the grade for midterm
# Validate the input as a float between 0 and 100
def get_midterm_grade():
    while True:
        midterm_grade = input("Enter your midterm grade (0-100): ")
        try:
            midterm_grade = float(midterm_grade)
            if 0 <= midterm_grade <= 100:
                return midterm_grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")


# 5 marks
# Prompt the user to enter the grade for exam
# Validate the input as a float between 0 and 100

def get_exam_grade():
    while True:
        try:
            exam_grade = float(input("Enter your exam grade (0-100): "))
            if 0 <= exam_grade <= 100:
                return exam_grade
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Invalid input, please enter a number")


# 10 marks
# Calculate the weighted average of each assessment component: Assignments, Midterm, Exam
# Calculate the percent grade as specified in the course outline
# https://www.wikihow.com/Calculate-Weighted-Average

# Thanks a lot !!!

# 2 marks
# Calculate letter grade (call the appropriate function)
def calculate_alpha_grade(percent_grade):
    letter_grade = calculate_alpha_grade(percent_grade)
    return letter_grade

# 3 marks
# Display the data as shown in the sample output

print("Student Information")
print(get_student_info())
print("----------------------")
print("Course Information")
print(get_course_info())
print("----------------------")
print("Mark Breakdown" )
