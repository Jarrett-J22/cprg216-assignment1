print("Welcome to the Grade Registry")
students = {}

while True:
    choice = input("Would you like to add a new student? y(yes),n(no)\n")

    if choice.lower() == "n" or choice.lower() == "no":
        break
    elif choice.lower() == "y" or choice.lower() == "yes":
        name = input("Enter the student's name:\n")
        print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")

        gpas = []
        while True:
            gpa_input = input()
            if gpa_input == "-1":
                break
            gpas.append(float(gpa_input))

        if len(gpas) > 0:
            avg = sum(gpas) / len(gpas)
        else:
            avg = 0

        students[name] = avg
    else:
        print("Incorrect Input, please enter y(yes)/n(no).")

print("This is the list of students in the system, and their average GPA")
for name in students:
    print(name, round(students[name], 2))
