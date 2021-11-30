# 8 kyu
# convert a number to reversed array of digits


def digitize(n):
    return [int(i) for i in str(n)[::-1]]
    # slicing the string from the end to the beginning
    # list[start:stop:step]
    

