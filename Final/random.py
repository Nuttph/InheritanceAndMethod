import random

def random_value(choices):
    """สุ่มเลือกค่าในรายการ choices"""
    return random.choice(choices)

# ตัวอย่างการใช้งาน
options = ['apple', 'banana', 'cherry', 'date']
result = random_value(options)
print("Random choice:", result)
