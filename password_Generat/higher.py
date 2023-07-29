student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_number = 0

for number in student_scores:
  if number > highest_number:
    highest_number = number

# highest_number = str(highest_number) 
# print("The highest score in the class is: " + highest_number)

print(f"The highest score in the class is: {highest_number}")

# print(max(student_scores))
# print(min(student_scores))



    
  
  
  
  
  