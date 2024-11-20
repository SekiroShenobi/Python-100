# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   TYoung,11/19/2024,Created Script
#  
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
students: list = []  # List to hold student records
menu_choice: str  # Hold the choice made by the user.

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        students.append([student_first_name, student_last_name, course_name])
        print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")

    # Present the current data
    elif menu_choice == "2":
        if not students:
            print("\nNo data available.")
        else:
            print("\nThe current data is:")
            for student in students:
                print(f"{student[0]} {student[1]} is enrolled in {student[2]}")

    # Save the data to a file
    elif menu_choice == "3":
        with open(FILE_NAME, "w") as file_obj:
            for student in students:
                file_obj.write(f"{student[0]},{student[1]},{student[2]}\n")
        print(f"\nData has been saved to {FILE_NAME}")

    # Stop the loop
    elif menu_choice == "4":
        print("\nThank you for using the Course Registration Program!")
        break

    else:
        print("\nPlease only choose option 1, 2, 3, or 4")

print("Program Ended")
