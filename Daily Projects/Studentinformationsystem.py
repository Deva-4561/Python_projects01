students = []

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        students.append({"Name": name, "Age": age, "Grade": grade})
        print(f"Student {name} added.")

    elif choice == '2':
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for i, student in enumerate(students, 1):
                print(f"{i}. Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")