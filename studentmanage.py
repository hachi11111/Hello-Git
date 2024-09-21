import sys
class Student:
    def __init__(self, name, age, gender, student_id, hobbies, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.hobbies = hobbies
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, ID: {self.student_id}, Hobbies: {self.hobbies}, GPA: {self.gpa}"
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def sort_students(self, by='name'):
        if by == 'name':
            self.students.sort(key=lambda x: x.name)
        elif by == 'age':
            self.students.sort(key=lambda x: x.age)
        elif by == 'gpa':
            self.students.sort(key=lambda x: x.gpa, reverse=True)

    def save_students(self, filename):
        with open(filename, 'w') as file:
            for student in self.students:
                file.write(f"{student.name},{student.age},{student.gender},{student.student_id},{student.hobbies},{student.gpa}\n")

    def load_students(self, filename):
        self.students = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                student = Student(data[0], int(data[1]), data[2], data[3], data[4], float(data[5]))
                self.students.append(student)

    def view_students(self):
        for student in self.students:
            print(student)
import sys

def print_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Sort Students")
    print("4. Save Students")
    print("5. Load Students")
    print("6. View Students")
    print("7. Exit")

def main():
    sms = StudentManagementSystem()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            student_id = input("Enter student ID: ")
            hobbies = input("Enter hobbies: ")
            gpa = float(input("Enter GPA: "))
            sms.add_student(Student(name, age, gender, student_id, hobbies, gpa))
            print("Student added successfully.")

        elif choice == '2':
            student_id = input("Enter student ID to delete: ")
            sms.delete_student(student_id)
            print("Student deleted successfully.")

        elif choice == '3':
            sort_by = input("Sort by (name/age/gpa): ")
            sms.sort_students(by=sort_by)
            print("Students sorted successfully.")

        elif choice == '4':
            filename = input("Enter filename to save: ")
            sms.save_students(filename)
            print("Students saved successfully.")

        elif choice == '5':
            filename = input("Enter filename to load: ")
            sms.load_students(filename)
            print("Students loaded successfully.")

        elif choice == '6':
            sms.view_students()

        elif choice == '7':
            print("Exiting...")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
