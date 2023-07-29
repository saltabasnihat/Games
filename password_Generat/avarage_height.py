# You are going to write a program that calculates the average
# student height from a List of heights.


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum_height = 0
for n in student_heights:
  sum_height += n

number_inputs = 0
for k in student_heights:
  number_inputs += 1


avarege_height = sum_height / number_inputs
print(round(avarege_height))


# total_height = sum(student_heights)
# number_students = len(student_heights)
# avarege_height = round(total_height / number_students)
# print(avarege_height)
  
