from oop import Student

st = [
    Student("Sanjar", 15, 73, "male"),
    Student("Umar", 16, 73, "male"),
    Student("Rashid", 18, 73, "male"),
    Student("Gulnora", 19, 73, "male"),
    Student("Mansur", 22, 73, "male"),
    Student("Maksim", 22, 73, "male"),
    Student("Samad", 24, 73, "male"),
    Student("Nigora", 26, 73, "female"),
    Student("Raxim", 29, 73, "male"),
]

# a=12
# b=56
# a,b=b,a
#
# print(a,b)

a = [5, 8, 1, 12, 15, 10, 4]


def buble_sort(a):
    for i in range(0, len(a) - 1):
        print(a)
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a


a1 = buble_sort(a)
print("Result",a1)
