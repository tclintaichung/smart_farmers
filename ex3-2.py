def triangle_area(base, height):
    """計算三角形面積"""
    return (base * height) / 2

# 主程式
b = float(input("請輸入三角形的底: "))
h = float(input("請輸入三角形的高: "))

area = triangle_area(b, h)
print("三角形的面積為:", area)
