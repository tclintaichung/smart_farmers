# 電影分級判斷程式
# 使用者輸入年齡，程式輸出適合的分級

def movie_rating(age):
    if age < 6:
        return "限制：僅限家長陪同 (幼兒不建議觀看)"
    elif age < 12:
        return "普遍級 (G) - 適合所有年齡"
    elif age < 15:
        return "保護級 (PG) - 建議家長陪同"
    elif age < 18:
        return "輔導級 (PG-13 / R-15) - 需家長同意"
    else:
        return "限制級 (R-18) - 成人可自由觀看"

# 主程式
try:
    age = int(input("請輸入您的年齡: "))
    print("您的電影分級為:", movie_rating(age))
except ValueError:
    print("請輸入正確的數字！")
