# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F(below 60).

score = 96

# exit()    // exits the python program

if score <= 100 and score >= 90:
    print("A")
elif score <= 89 and score >= 80:
    print("B")
elif score <= 79 and score >= 70:
    print("C")
elif score <= 69 and score >= 60:
    print("D")
else:
    print("F")

