from oop import Student

st=[
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


def binary_search(st, val):
    l=0
    h=len(st)-1
    while h>=l:
        m=(h+l)//2
        if st[m].get_age()==val:
            return m
        elif st[m].get_age()>val:
            h=m-1
        else:
            l=m+1
    return None

ind=binary_search(st,22)
if ind:
    st[ind].print()
else:
    print("Student not found!")


# for s in st:
#     if s.get_age()==24:
#         s.print()