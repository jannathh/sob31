# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #added "int" before input because the input taken in is an integer

exam_three = int(input("Input exam grade three: ")) #changed the variable name exam_3 to exam_three to match the previously assigned varibale names 
#also changed "str" to "int" because the input taken in is an integer and not a string

grades = [exam_one, exam_two, exam_three] #added commas to seperate the values in the list
sum = 0
for grade in grades: #changed "grade" to "grades"
  sum = sum + grade

avg = sum / len(grades) #spelling error corrected to "grades"

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added missing colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #changed the single quote to double quotes at the end
elif avg >= 69 and avg > 70: #corrected the logical error; changed "<= 69" to ">= 69", and ">= 65" to "< 70" 
    letter_grade = "D"
else: #changed "elif" to "else"
    letter_grade = "F"

print("Exam: " + str(exam_one) + ", ", str(exam_two), ", ", str(exam_three))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": #replaced hyphen with underscore for letter_grade
#also changed "is" to "=="
    print ("Student is failing.") #added missing brackets
else:
    print ("Student is passing.") #added missing brackets
