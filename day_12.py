# def read_file(path):
#     with open(path, "r") as f:
#         return f.read()
    

# def interpret_content(path):
#     content = read_file(path)
#     student_info = {}
#     for line in content.splitlines("\n"):
#         name, marks = line.split(",")
#         student_info[name] = float(marks)

#     avg = sum(student_info.values()) / len(student_info)
#     student_information = " ,".join(student_info.keys())
#     print("Student Information: ",student_information)
#     print("Average Marks: ",avg)


# interpret_content("grades.txt")


def check_password(path):
    with open(path, "r") as f:
        password = f.read()
    for passw in password.splitlines():
        if len(passw) < 8:
            print(f"Password '{passw}' is too short. It should be at least 8 characters long.")
        elif not any(char.isdigit() for char in passw):
            print(f"Password '{passw}' should contain at least one digit.")
        elif not any(char in "!@#$%^&*()-+" for char in passw):
            print(f"Password '{passw}' should contain at least one special character.")
        else:
            print(f"Password '{passw}' is strong password.")
            
check_password("test_passwords.txt")

