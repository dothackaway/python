students = []

def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception as error:
        print("Could not read file")
        print(error)

def read_students(f):
    for line in f:
        yield line

read_file()
print(students)