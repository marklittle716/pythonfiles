#creating a class


class User:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

Student1 = User('Tony', 39, 72, 209)

print(Student1.age)
print(Student1.name)


#freaking Git push finally worked