

def digital_func_Sum(n):
    if n < 10:
        return n
    return n % 10 + digital_func_Sum( n // 10 )

print(digital_func_Sum(2347623) == 27)

