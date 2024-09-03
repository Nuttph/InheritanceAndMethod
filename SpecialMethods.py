class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

# สร้างวัตถุ Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# ใช้เมธอด __lt__ เปรียบเทียบ
print(person1 < person2)  # Output: False
print(person1 == person2)  # Output: False
