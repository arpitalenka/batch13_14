students = [("Arpita" ,80),
            ("Priyaranjan",95),
            ("Mamata",98),
            ("Ayush",78)
]


def sort_students(stu):
    return stu[1]

students.sort(key=sort_students, reverse=True)
print(students)