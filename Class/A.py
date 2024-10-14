class A:
    def __init__(self,n,a): #special method
        #set variable
        self.name = n
        self.__age = a

    def ReturnInfo(self): #public
        print(f'name : {self.name}\nage : {self.__age}')
    
    def ReturnPri(self):
        return self.__age

    def __str__(self):
        return f'hello welcome str'

class B(A):
    def __init__(self,n,a):
        super().__init__(n,a)
    def rere(self):
        return self.name
    

Mai = B('Patima',50)
Mai.ReturnInfo()
# print(Mai)
print(Mai.rere())