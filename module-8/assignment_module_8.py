import json

# simple function that loops through the list of students and prints out each value.
def print_students(class_list):
    for student in class_list: 
        first_name = student["F_Name"]
        last_name = student["L_Name"]
        student_id = student["Student_ID"]
        email = student["Email"]

        # Make formatted string like this: Ripley, Ellen: ID = 45604, Email = eripley@gmail.com
        print(f"{last_name}, {first_name}: ID = {student_id}, Email = {email}")

with open('Student.json', 'r') as f:
    student_list = json.load(f)
    print("\nThis is the original student list.\n")
    print_students(student_list)

    # add my name, last name, etc, call append
    student_list.append({"F_Name": "Jasmine", "L_Name": "Fontus", "Student_ID": 12345, "Email": "jfontus@my365.bellevue.edu"})

    print("\nThis is the updated student list.\n")
    print_students(student_list)

    with open('Student.json', 'w') as write_file:
        json.dump(student_list, write_file)

    print("\nThe json file was updated.\n")