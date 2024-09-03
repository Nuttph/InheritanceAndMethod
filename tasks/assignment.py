class BankAccount:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def __lt__(self, other):
        return self.money < other.money

    def __repr__(self):
        return f'BankAccount(name={self.name!r}, money={self.money!r})'

    def __str__(self):
        return f'{self.name} has {self.money}'

# สร้างบัญชีธนาคารแต่ละบัญชี
account1 = BankAccount("kik", 200)
account2 = BankAccount("cathy", 300)
account3 = BankAccount("numwan", 500)

# เก็บบัญชีทั้งหมดในลิสต์
accounts = [account1, account2, account3]

# หา account ที่มีเงินมากที่สุด
max_account = accounts[0]  # เริ่มต้นด้วย account แรก
for account in accounts:
    if max_account < account:  # ถ้า max_account มีเงินน้อยกว่า account ปัจจุบัน
        max_account = account

print(f'Person with the most money: {max_account.name} with {max_account.money}')

# เรียงลำดับจากมากไปน้อยโดยใช้การเปรียบเทียบ __lt__
sorted_accounts = []
while accounts:
    max_account = accounts[0]
    for account in accounts:
        if max_account < account:
            max_account = account
    sorted_accounts.append(max_account)
    accounts.remove(max_account)

# แสดงผลลัพธ์
for account in sorted_accounts:
    print(account)
