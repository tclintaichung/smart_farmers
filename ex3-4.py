# 建立字典
student = {
    "id": "S001",
    "name": "Alice",
    "age": 14,
    "grade": "8th"
}

# 取值
print(student["name"])   # 輸出: Alice

# 新增或修改
student["age"] = 15
student["address"] = "Taichung"

# 刪除
del student["grade"]

print(student)
