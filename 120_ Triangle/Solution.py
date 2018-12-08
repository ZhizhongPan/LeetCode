def divide_coquer_recu(i, j, triangle):
    if i == len(triangle):
        return 0
    
    return triangle[i][j]+ min(
        divide_coquer_recu(i+1, j, triangle),
        divide_coquer_recu(i+1, j+1, triangle))

def dp_down_top(triangle):
    if len(triangle) == 0:
        return 0

    result = triangle[-1]
    for level in range(len(triangle)-2, -1, -1):
        for i in range(0, level+1):
            result[i] = triangle[level][i] + min(result[i], result[i+1])

    return result[0]

def dp_top_down(triangle):
    pass
    



    







