import json

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"学生 {student['name']} 添加成功！")

    def delete_student(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                self.students.remove(student)
                print(f"学生 {student['name']} 删除成功！")
                return
        print(f"未找到学号为 {student_id} 的学生！")

    def sort_students(self, key="name"):
        self.students.sort(key=lambda x: x[key])
        print(f"学生信息已按 {key} 排序！")

    def save_students(self, filename="students.json"):
        with open(filename, 'w') as f:
            json.dump(self.students, f, indent=4)
        print(f"学生信息已保存到 {filename}！")

    def load_students(self, filename="students.json"):
        try:
            with open(filename, 'r') as f:
                self.students = json.load(f)
            print(f"学生信息已从 {filename} 加载！")
        except FileNotFoundError:
            print(f"文件 {filename} 不存在，未加载任何信息。")

    def view_students(self):
        if not self.students:
            print("当前没有学生信息！")
        else:
            for student in self.students:
                print(f"姓名: {student['name']}, 年龄: {student['age']}, 性别: {student['gender']}, 学号: {student['student_id']}, 爱好: {', '.join(student['hobbies'])}, 绩点: {student['gpa']}")

def main():
    manager = StudentManager()

    while True:
        print("\n学生信息管理系统")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查看学生")
        print("4. 排序学生")
        print("5. 保存学生信息")
        print("6. 加载学生信息")
        print("7. 退出")

        choice = input("请输入选项: ")

        if choice == "1":
            name = input("姓名: ")
            age = int(input("年龄: "))
            gender = input("性别: ")
            student_id = input("学号: ")
            hobbies = input("爱好 (用逗号分隔): ").split(",")
            gpa = float(input("绩点: "))

            student = {
                "name": name,
                "age": age,
                "gender": gender,
                "student_id": student_id,
                "hobbies": hobbies,
                "gpa": gpa
            }
            manager.add_student(student)

        elif choice == "2":
            student_id = input("请输入要删除的学生的学号: ")
            manager.delete_student(student_id)

        elif choice == "3":
            manager.view_students()

        elif choice == "4":
            key = input("请输入排序依据 (name, age, gpa): ")
            manager.sort_students(key)

        elif choice == "5":
            filename = input("请输入保存文件名 (默认为 students.json): ") or "students.json"
            manager.save_students(filename)

        elif choice == "6":
            filename = input("请输入加载文件名 (默认为 students.json): ") or "students.json"
            manager.load_students(filename)

        elif choice == "7":
            print("退出系统。")
            break

        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()
