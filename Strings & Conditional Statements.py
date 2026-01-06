## WAP to input users first name and print its length

name = input("Enter your name: ")
print ("Length of your name is", len(name))


#WAP to grade marks

marks = int(input("Enter your marks : "))

if (marks>=90):
  grade = "A"

elif (marks>= 80 and marks < 90):
  grade = "B"
elif (marks>=70 and marks <80):
  grade = "C"
else:
  grade = "D"

print("grade of the students :", grade)


#WAP whether the number is even or odd

num = int (input("Enterb a number: "))

if num % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")