def pascal_triangle(n):
    my_list = []
    if n > 0:
        my_list.append([1])
        for i in range(1, n):
            x = my_list[i - 1]
            my_list.append([1] + [x[j] + x[j + 1] for j in range(len(x) - 1)] + [1])
                
        return my_list
    else:
        return my_list
