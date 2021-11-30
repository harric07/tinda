# 8kyu
# If you can't sleep, just count sheep!!


'''
Given a non-negative integer,
3 for example, return a string with a murmur:
"1 sheep...2 sheep...3 sheep...".
Input will always be valid,
i.e. no negative integers.

'''



def count_sheep(n):
    r = ''
    for i in range(1, n+1):
        r += str(i) + ' sheep...'
    return r


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))




