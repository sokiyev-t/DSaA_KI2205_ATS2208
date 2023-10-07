
class Person:
    name = "Amir"
    _age = 20
    _weigh = 74
    sex = "male"

    def get_weigh(self):
        return self._weigh

    def set_weigh(self, w):
        if w > 0:
            self._weigh = w

    def get_age(self):
        return self._age

    def set_age(self, a):
        if a > 0:
            self._age = a

    def print(self):
        print(f"Name: {self.name}; \nAge: {self._age}; \nWeigh: {self._weigh}")

    def __init__(self, name, age, weigh, sex):
        self.name = name
        self._age = age
        self._weigh = weigh
        self.sex = sex


class Employee(Person):
    salary=200000


class Student(Person):
    group=214

    def print(self):
        print(f"Group: {self.group};\nName: {self.name}; \nAge: {self._age}; \nWeigh: {self._weigh}")
    pass

s1=Student("Sanjar", 26, 73, "male")
s2=Student("Gulnora", 19, 60, "female")
e1=Employee("Samad", 22, 74, "male")
e2=Employee("Nigora", 22, 74, "famale")
e3=Employee("Madina", 22, 74, "female")
e4=Employee("Mansur", 17, 71, "male")

a=[s1,s2,e1,e2,e3,e4]

for p in a:
    if p.get_age()>18 and p.sex=="male":
        print("--------------------------")
        p.print()




T sum<T>(T a, T b) {
    return a+b;
}


int k=sum<int>(3,4);

Vector<int> v;



# def my_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# c = 17
# a = 25
# d = my_max(c, a)
# print("Result: ", d)
