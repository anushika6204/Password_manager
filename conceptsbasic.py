#CONCEPTS
#CONDITIONAL - to implement a logic
#LOOPS - menu system
#DICTIONARY - store data

student = {}
while True:
    print("\n----STUDENT MANAGDER APP----")
    print("1. Add Student")
    print("2. view Student")
    print("3. check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")

    #view student
    elif choice == "2":
        if not student:
            print("no student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    #check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("Student Not found! ")

    #exit
    elif choice == "4":
        print("Existing....")
        break

    else:
        print("In-Valid input")











