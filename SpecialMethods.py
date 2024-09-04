#Python Polymorphism

class Example:
    def __init__(self,num): # function แรกที่จะทำเมื่อเรียกใช้ class นี้ // e1 = Example()
        self.num = num

    def __str__(self):
        return f'Hello world {self.num}' # function ที่จะทำเมื่อ print(ตัวแปรที่รับ class นี้) print(e1)
    
    def __repr__(self):
        return f'Example(number)' # __repr__ ใช้สำหรับแสดงข้อมูลที่ละเอียดและเหมาะสมสำหรับการดีบัก. print(repr())
    
    def __add__(self,other):
        return self.num + other.num

    def __sub__(self,other):
        return self.num - other.num
    
    def __mul__(self,other):
        return self.num*other.num
    
    def __pow__(self,other):
        return self.num**other.num
    
    def __truediv__(self,other):
        return self.num / other.num
    
    def __floordiv__(self,other):
        return self.num // other.num

    def __mod__(self,other):
        return self.num % other.num
    
    def __lshift__(self,other):
        return self.num << other.num
    
    def __rshift__(self,other):
        return self.num >> other.num

    def __and__(self,other):
        return self.num & other.num
    
    def __or__(self,other):
        return self.num | other.num
    
    def __xor__(self,other):
        return self.num ^ other.num
    
    def __invert__(self):
        return ~self.num

e1 = Example(19)
e2 = Example(20)

print(e1+e2)