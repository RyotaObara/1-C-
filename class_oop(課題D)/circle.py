# 課題D-1: 円オブジェクト
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # 面積を計算するメソッド (面積 = π * r^2)
    def area(self):
        return round(math.pi * (self.radius**2), 2)

    # 周囲長を計算するメソッド (周囲長 = 2 * π * r)
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())


# 課題D-2: 長方形オブジェクト
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 面積 (縦 × 横)
    def area(self):
        res = self.height * self.width
        return f"{res:.2f}"

    # 対角線 (√(縦^2 + 横^2))
    def diagonal(self):
        # ** 0.5 でルート（平方根）を計算
        res = (self.height**2 + self.width**2) ** 0.5
        return f"{res:.2f}"


#
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24


# 課題D-3: 正方形オブジェクト
class Square:
    def __init__(self, side):
        self.side = side

    # 面積を計算 (一辺 × 一辺)
    def area(self):
        res = self.side**2
        # 出力例に合わせて、整数ならそのまま、小数なら必要な形式にします
        return int(res) if res.is_integer() else res

    # 対角線の長さを計算 (√(side^2 + side^2))
    def diagonal(self):
        # 三平方の定理: side * √2
        res = (self.side**2 + self.side**2) ** 0.5
        # 小数点2桁でフォーマット
        return f"{res:.2f}"


# --- 動作確認 ---
square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21


# 課題D-4: カウンターその1
class MyCounterV1:
    def __init__(self, value):
        # 初期値をインスタンス変数に保存
        self.value = value

    def count_up(self):
        # メソッドが呼ばれるたびに value を 1 増やす
        self.value += 1


# --- 動作確認 ---

# counter1 の動き
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

# counter2 の動き（初期値が異なる）
counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9

# 課題D-5: カウンターその2
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # 面積 = πr^2
        return f"{math.pi * self.radius**2:.2f}"

    def perimeter(self):
        # 周囲長 = 2πr
        return f"{2 * math.pi * self.radius:.2f}"


# 課題D-6: カウンターその3
class MyCounterV3:
    def __init__(self, value, step):
        # 初期値と、増減の幅(step)をインスタンス変数に保存します
        self.value = value
        self.step = step

    def count_up(self):
        # 現在の値に step 分だけ加算します
        self.value += self.step

    def count_down(self):
        # 現在の値から step 分だけ減算します
        self.value -= self.step


# --- 以下、ご提示いただいたテストコードでの動作確認 ---
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3 (1 + 2)

counter1.count_up()
print(counter1.value)  # 5 (3 + 2)

counter1.count_down()
print(counter1.value)  # 3 (5 - 2)

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1 (3 - 4)

counter2.count_down()
print(counter2.value)  # -5 (-1 - 4)
