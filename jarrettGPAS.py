students = {}

print("Welcome to the Grade Registry Program")

continue_option = input("Would you like to add a new student? y(yes),n(no)\n")

while continue_option == "y" or continue_option == "yes":
    name = input("\nEnter the student's name:\n")

    gpas = []
    print("\nEnter student GPA for each subject. Enter -1 to stop entering GPA.")

    while True:
        gpa_input = input()
        if gpa_input == "-1":
            break
        else: 
            gpa = float(gpa_input)
            gpas.append(gpa)
      

    students[name] = gpas

    continue_option = input("\nWould you like to add a new student? y(yes),n(no)\n")

    while continue_option not in ["y", "yes", "n", "no"]:
        print("Incorrect Input, please enter y(yes)/n(no).")
        continue_option = input("Would you like to add a new student? y(yes),n(no)\n")

# Final output
print("\nThis is the list of students in the system, adn their corresponding accumulative GPA")
for name, gpas in students.items():
    if len(gpas) >0:
        averagegpa = sum(gpas)/len(gpas)
        print(name, averagegpa)
    else: 
        print(name, "0")