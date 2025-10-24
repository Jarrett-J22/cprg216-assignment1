print("Welcome to the Grade Registry")

students = {}  

while True:
    print("Would you like to add a new student? y(yes),n(no)")
    choice = input()  

    if choice == "n" or choice == "no":
        break

    elif choice == "y" or choice == "yes":
        print("Enter the student's name:")
        name = input()

        print("Enter the student's GPA (e.g., 3.5):")
        gpa_input = input()          
        gpa = float(gpa_input)       

        students[name] = gpa         

    else:
        print("Incorrect input, please enter y(yes)/n(no).")

print("This is the list of students in the system and their GPA:")
for name in students:
    print(name, students[name])

input("Press Enter to exit.")
