class Person:
    def __init__(self,name):
        self.name = name

    def PersonName(self):
        return f'name: {self.name}' #name: Nuttaphon
    
class Student(Person):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
    
    def __str__(self):
        return f'name: {self.name}\nid: {self.id}' #name: Nuttaphon id: 663
    

s1 = Student('Nuttaphon',663)
print(s1) #output name: Nuttaphon id: 663
print(s1.PersonName()) #name: Nuttaphon