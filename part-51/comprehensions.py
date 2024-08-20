students = [("Arpita" ,80),
            ("Priyaranjan",95),
            ("Mamata",98),
            ("Ayush",78)
]


# map function
names = list(map(lambda x: x[0], students))

#new_names = [statement for x in list]
new_names = [x[0]for x in students]

print(new_names)

#filter function
new_list = filter(lambda x: x[1] > 90, students)

#list1 = [statement for x in list condition]
list1 = [ x for x in students if x[1] > 90]

print(list1)