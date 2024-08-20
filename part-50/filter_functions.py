students = [("Arpita" ,80),
            ("Priyaranjan",95),
            ("Mamata",98),
            ("Ayush",78)
]

new_list = filter(lambda x: x[1] > 90, students)
new_list = list(new_list)
print(new_list)