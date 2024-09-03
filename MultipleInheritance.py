class Person:
    def __init__(self,name):
        self.name = name

    def PersonName(self):
        return f'name: {self.name}' #name: Nuttaphon
    
class VIPs():
    def __init__(self,passed):
        self.passed = passed
    def SecretPass(self):
        return f'secret pass: {self.passed}'

class Student(Person,VIPs):
    def __init__(self,name,id,passed):
        Person.__init__(self,name)
        VIPs.__init__(self,passed)
        self.id = id
    
    def __str__(self):
        return f'name: {self.name}\nid: {self.id}\nsecret pass: {self.passed}' #name: Nuttaphon id: 663
    

s1 = Student("Nuttaphon",663,00000000)
print(s1) #output name: Nuttaphon id: 663 secret pass: 00000000 

print(s1.SecretPass()) #output secret pass: 00000000