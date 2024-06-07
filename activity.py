## Prompts the user to enter a score.

score = int(input("Enter your score (0-100): "))
## Determines the grade based on the user input or score.
if score >= 80:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade for your score {score} is {grade}") 