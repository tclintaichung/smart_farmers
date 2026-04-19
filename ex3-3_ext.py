from functools import reduce

def odd(a):
    return a % 2 == 1

def sqrt_func(a):
    return a * a

def sum_func(a, b):
    return a + b

a_list = [1, 2, 3, 4, 5, 6]

odd_nums = filter(odd, a_list)
sqrt_nums = map(sqrt_func, a_list)
sum_nums = reduce(sum_func, a_list)

for item in odd_nums:
    print(item)
    
for item in sqrt_nums:
    print(item)
    
print("Sum of all elements: " + str(sum_nums))