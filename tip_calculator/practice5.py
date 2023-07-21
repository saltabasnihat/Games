# Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_h = float(height)
new_w = float(weight)

bmi = new_w / (new_h ** 2)

print(int(bmi))
