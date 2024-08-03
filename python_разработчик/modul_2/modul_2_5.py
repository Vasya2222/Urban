
def get_matrix(n: int, m: int, value: int) -> list[int]:
    matrix = list()

    if n <= 0 or m <= 0:
        return []
    
    for i in range(n):
        second_list = list()
        for j in range(m):
            second_list.append(value)
        matrix.append(second_list)
    
    
    
    return matrix

result1 = get_matrix(2, -2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)