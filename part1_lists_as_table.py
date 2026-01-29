"""Part 1: Lists as Tables
Each row is a list: [id, name, school, credits]
Schema is implicit — your code depends on correct indexes.
"""

students = [
    [1, "Alice", "GSAS", 32],
    [2, "Bob", "Tandon", 28],
    [3, "Carol", "GSAS", 40],
    [4, "Dan", "CAS", 18]
]
# columns: [id, name, school, credits]


# TODO 1: Print all student names (one per line)
print("All student name:",students[0][1],students[1][1],students[2][1],students[3][1])
# TODO 2: Print only the students in GSAS (id and name)
for each_stu in students:
    school=each_stu[2]
    if school=="GSAS":
        print(each_stu[1])

# TODO 3: Print students with credits > 30 (name and credits)
for each_stu in students:
    credit=each_stu[3]
    if credit>30:
        print("Student name with credits>30:",each_stu[1],"Credit:",each_stu[3])

# TODO 4: Insert a new student row for: id=5, name='Eve', school='CAS', credits=22
students.append([5, "Eve", "CAS", 22])
print(students)

# TODO 5: Update Bob’s credits to 30
for each_stu in students:
    if each_stu[1]=="Bob":
        each_stu[3]=30
print(students)


# Reflection (answer in a comment):
# TODO: What breaks if we insert a new column at position 2?
