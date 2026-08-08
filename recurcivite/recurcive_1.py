def sum_recursive(num):
    if num == 1:  # Base case
        return num
    return num + sum_recursive(num - 1)  # Recursive case

print(sum_recursive()) # 3 + 2 + 1 