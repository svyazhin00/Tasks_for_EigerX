def func_max(x=None, count=1):
    try:
        i = int(input())
        if i == 0:
            return x, count
        else:
            if x is None:
                x = i
                count = 1
                return func_max(x, count)
            else:
                if i < x:
                    return func_max(x, count)
                elif i > x:
                    return func_max(i, count)
                else:
                    count += 1
                    return func_max(i, count)
    except:
        raise TypeError('Type must be integer!')

print(func_max())
