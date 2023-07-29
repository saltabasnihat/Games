# You are going to write a program that calculates the sum of
# all the even numbers from 1 to 100. Thus, the 
# first even number would be 2 and the last one is 100:



total_number = 0

for number in range(2,101,2):
    total_number += number

print(total_number)

