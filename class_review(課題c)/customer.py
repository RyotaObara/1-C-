# Feature
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# C-1. フルネームを取得できる
print(ken.full_name())
print(tom.full_name())
print(ieyasu.full_name())


# C-2. 年齢という概念の追加
print(ken.age)
print(tom.age)
print(ieyasu.age)


# C-3. 入場料の確認
print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(ieyasu.info_csv())

