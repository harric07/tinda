

# ord = ordinal number, it returns the unicode number of the string character based on the ascii table
# chr = character, it returns the string character of the unicode number.

# ASCII key codes:
# lowercase: 97-122
# 26 characters 
# a = 97, b = 98, c = 99, d = 100, e = 101, f = 102, 
# g = 103, h = 104, i = 105, j = 106, k = 107, l = 108, 
# m = 109, n = 110, o = 111, p = 112, q = 113, r = 114, 
# s = 115, t = 116, u = 117, v = 118, w = 119, x = 120, 
# y = 121, z = 122

# uppercase: 65-90
# A = 65, B = 66, C = 67, D = 68, E = 69, 
# F = 70, G = 71, H = 72, I = 73, J = 74, 
# K = 75, L = 76, M = 77, N = 78, O = 79, P = 80, 
# Q = 81, R = 82, S = 83, T = 84, U = 85, V = 86, 
# W = 87, X = 88, Y = 89, Z = 90

#number: 48-57
# 0 = 48, 1 = 49, 2 = 50, 3 = 51, 4 = 52, 
# 5 = 53, 6 = 54, 7 = 55, 8 = 56, 9 = 57

# punctuation: 33-47, 58-64, 91-96, 123-126
# space = 32, ! = 33, " = 34, # = 35, $ = 36, 
# % = 37, & = 38, ' = 39, ( = 40, ) = 41, 
# * = 42, + = 43, , = 44, - = 45, . = 46, 
# / = 47, : = 58, ; = 59, < = 60, = = 61, 
# > = 62, ? = 63, @ = 64, [ = 91, \ = 92, 
# ] = 93, ^ = 94, _ = 95, ` = 96, 
# { = 123, | = 124, } = 125, ~ = 126

# \n = 10, \r = 13, \t = 9
# \b = 8, \f = 12, \v = 11
# \0 = 0, \1 = 1, \2 = 2, \3 = 3, \4 = 4, \5 = 5, \6 = 6, \7 = 7, \8 = 8, \9 = 9, \10 = 10, \11 = 11, \12 = 12, \13 = 13, \14 = 14, \15 = 15, \16 = 16, \17 = 17, \18 = 18, \19 = 19, \20 = 20, \21 = 21, \22 = 22, \23 = 23, \24 = 24, \25 = 25, \26 = 26, \27 = 27, \28 = 28, \29 = 29, \30 = 30, \31 = 31


'''replace every letter with its position in the alphabhet, where a = 1, b = 2, etc.'''

def alphabet_position(x):
    '''replace every letter with its position in the alphabhet, where a = 1, b = 2, etc.'''
    x = x.lower()
    y = " "
    for i in x:
        if i.isalpha():
            y += str(ord(i) - 96) + " "
    return y.strip()




'''
function unique_in_order 
which takes as argument a sequence 
and returns a list of items 
without any elements with the same value 
next to each other 
and preserving the original order of elements.
'''

unique_in_order = lambda x: [x[i] for i in range(len(x)) if i == 0 or x[i] != x[i-1]]
unique_in_order('AAAABBBCCDAABBB')

# sequence = iterable + ordered collection
# iteratable = list, tuple, string, set, dictionary

def unique_in_order(x):
    y = []
    for i in range(len(x)):
        if i == 0 or x[i] != x[i-1]:
            y.append(x[i])
    return y

# unique_in_order('ABBCcAD')


'''
Given an array of ones and zeroes, 
convert the equivalent binary value to an integer.
'''
# covert array of 1s and 0s to binary value of interger.
def convert_array_to_binary(x):
    y = 0
    for i in range(len(x)):
        y += x[i] * (2 ** (len(x) - i - 1))
    return y

'''
You will be given an array of numbers. 
You have to sort the odd numbers in ascending order 
while leaving the even numbers at their original positions
'''
def sort_array_asc(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


'''
find the missing letter in consecutive alphabetical sequence
'''
def find_missing_letter(chars):
    x = ''
    for i in range(0,len(chars)-1):
        if (ord(chars[i+1]) - ord(chars[i]) > 1):
            x = chr(ord(chars[i]) + 1)
    return x


'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.
'''
def pig_it(text):
    x = ''
    for i in text.split(' '):
        if i[0].isalpha():
            x += i[1:] + i[0] + 'ay '
        else:
            x += i + ' '
    return x.strip()

'''
Write a function that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, 
and false if it's invalid.
'''
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0


'''
Write a function that takes a string of braces, 
and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.
All input strings will be nonempty, and will only consist of parentheses, 
brackets and curly braces: ()[]{}.
'''

def valid_braces(string):
    braces = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in string:
        if char in braces.keys():
            stack.append(char)
        elif char in braces.values():
            if not stack or braces[stack.pop()] != char:
                return False
    return not stack

'''
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n.
If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
16  -->  1 + 6 = 7
'''

def digital_root(n):
    return n if n < 10 else digital_root(sum(int(i) for i in str(n)))

'''
The new "Avengers" movie has just been released! 
There are a lot of people at the cinema box office standing in a huge line. 
f them has a single 100, 50 or 25 dollar bill. 
An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. 
He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to every person and 
give change if he initially has no money and 
sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and 
give change with the bills he has at hand at that moment. 
Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change 
(you can't make two bills of 25 from one of 50)
'''

def tickets(people):
    t25 = 0
    t50 = 0 
    t100 = 0
    for i in people:
        if i == 25: t25 += 1
        elif i == 50: t25 -= 1; t50 += 1
        elif i == 100 and t50>0 : t25 -=1; t50-=1
        elif i == 100 and t50 == 0: t25 -=3
        if t25<0 or t50<0:
            return 'NO'
    return 'YES'

def tickets(people):
    change = []
    try:
        for cash in people:
            if cash == 25:
                change.append(25)
            if cash == 50:
                change.remove(25)
                change.append(50)
            if cash == 100 and (50 in change):
                change.remove(50)
                change.remove(25)
            elif cash == 100:
                change.remove(25)
                change.remove(25)
                change.remove(25)
    except: 
        return "NO"
    else:
        return "YES"

'''
calculating with functions
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
'''

def zero(a='0'):
    if a != '0':
        if a[0]=='+':
            return 0+int(a[1])
        if a[0]=='-':
            return 0-int(a[1])
        if a[0]=='*':
            return 0*int(a[1])
        if a[0]=='/':
            return int(0/int(a[1]))
    else:
        return '0'
def one(a='1'):
    if a != '1':
        if a[0]=='+':
            return 1+int(a[1])
        if a[0]=='-':
            return 1-int(a[1])
        if a[0]=='*':
            return 1*int(a[1])
        if a[0]=='/':
            return int(1/int(a[1]))
    else:
        return '1'
def two(a='2'):
    if a != '2':
        if a[0]=='+':
            return 2+int(a[1])
        if a[0]=='-':
            return 2-int(a[1])
        if a[0]=='*':
            return 2*int(a[1])
        if a[0]=='/':
            return int(2/int(a[1]))
    else:
        return '2'
def three(a='3'):
    if a != '3':
        if a[0]=='+':
            return 3+int(a[1])
        if a[0]=='-':
            return 3-int(a[1])
        if a[0]=='*':
            return 3*int(a[1])
        if a[0]=='/':
            return int(3/int(a[1]))
    else:
        return '3'
def four(a='4'):
    if a != '4':
        if a[0]=='+':
            return 4+int(a[1])
        if a[0]=='-':
            return 4-int(a[1])
        if a[0]=='*':
            return 4*int(a[1])
        if a[0]=='/':
            return int(4/int(a[1]))
    else:
        return '4'
def five(a='5'):
    if a != '5':
        if a[0]=='+':
            return 5+int(a[1])
        if a[0]=='-':
            return 5-int(a[1])
        if a[0]=='*':
            return 5*int(a[1])
        if a[0]=='/':
            return int(5/int(a[1]))
    else:
        return '5'
def six(a='6'):
    if a != '6':
        if a[0]=='+':
            return 6+int(a[1])
        if a[0]=='-':
            return 6-int(a[1])
        if a[0]=='*':
            return 6*int(a[1])
        if a[0]=='/':
            return int(6/int(a[1]))
    else:
        return '6'
def seven(a='7'):
    if a != '7':
        if a[0]=='+':
            return 7+int(a[1])
        if a[0]=='-':
            return 7-int(a[1])
        if a[0]=='*':
            return 7*int(a[1])
        if a[0]=='/':
            return int(7/int(a[1]))
    else:
        return '7'
def eight(a='8'):
    if a != '8':
        if a[0]=='+':
            return 8+int(a[1])
        if a[0]=='-':
            return 8-int(a[1])
        if a[0]=='*':
            return 8*int(a[1])
        if a[0]=='/':
            return int(8/int(a[1]))
    else:
        return '8'
def nine(a='9'):
    if a != '9':
        if a[0]=='+':
            return 9+int(a[1])
        if a[0]=='-':
            return 9-int(a[1])
        if a[0]=='*':
            return 9*int(a[1])
        if a[0]=='/':
            return int(9/int(a[1]))
    else:
        return '9'
 
def plus(a):
    return '+'+a
def minus(a):
    return '-'+a
def times(a):
    return '*'+a
def divided_by(a):
    return '/'+a



def number_maker(n):
    def number(operator = None):
        if operator:
            return operator(n)
        else:
            return n
    return number

zero, one, two, three, four, five, six, seven, eight, nine = map(number_maker, range(10))

def plus(b): #your code here
   return lambda a : a + b
def minus(b):
    return lambda a : a - b
def times(b):
    return lambda a : a * b 
def divided_by(b): 
    return lambda a : a / b



'''
Memoized Fibonacci sequence:
recursive Fibonacci function that 
using a memoized data structure avoids 
the deficiencies of tree recursion to
make it so the memoization cache is 
private to this function.
'''
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    else:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        return cache[n]

'''
Product of consecutive Fibonacci numbers
'''
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]






'''
intergers: Recreation One

1, 246, 2, 123, 3, 82, 6, 41 
are the divisors of number 246. 
Squaring these divisors we get: 
1, 60516, 4, 15129, 9, 6724, 36, 1681. 
The sum of these squares is 84100 
which is 290 * 290.

Task
Find all integers between m and n 
(m and n integers with 1 <= m <= n) 
such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples 
(in C an array of Pair) or a string. 
The subarrays (or tuples or Pairs) 
will have two elements: 
first the number the squared divisors of which is a square 

and then the sum of the squared divisors.
'''

def list_squared(m, n):
    x =[]
    for i in range(m, n):
        d = [j**2 for j in range(1, i+1) if i % j == 0]
        sd = sum(d)
        q = sd**(1/2)
        if int(q) ** 2 == sd:
            x.append([i, sd])
    return x


'''
gap in prime numbers

The prime numbers are not regularly spaced. 
For example from 2 to 3 the gap is 1. 
From 3 to 5 the gap is 2. From 7 to 11 it is 4. 
Between 2 and 50 we have the following pairs 
of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive 
composite numbers between two successive primes 
(see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap 
we are looking for

m (integer > 2) which gives the start of 
the search (m inclusive)

n (integer >= m) which gives the end 
of the search (n inclusive)

n won't go beyond 1100000.

In the example above gap(2, 3, 50) 
will return [3, 5] or (3, 5) or {3, 5} 
which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first 
pair of two prime numbers spaced with a gap 
of g between the limits m, n if these numbers 
exist otherwise `nil or null or None or Nothing 
(or ... depending on the language).

In C++, Lua: return in such a case {0, 0}. 
In F#: return [||]. In Kotlin, Dart and Prolog: 
return []. In Pascal: return Type TGap (0, 0).
In Haskell: return Nothing. In Elixir: return []



'''

from math import ceil, sqrt

def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    else:
        return all(number % factor != 0
                for factor in range(3, ceil(sqrt(number)) + 1, 2))

def prime_generator(low, high):
    return [i for i in range(low, high+1) if is_prime(i)]

def gap(g, m, n):
    primes = prime_generator(m, n)
    for i in range(0, len(primes)-1):
        if primes[i+1] - primes[i] == g:
            return [primes[i], primes[i+1]]
    return None


'''
pick peak nummber in an array;

a function that returns the positions and the values 
of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] 
has a peak at position 3 with a value of 5 
(since arr[3] equals 5).

The output will be returned as an object 
with two properties: pos and peaks. 
Both of these properties should be arrays. 
If there is no peak in the given array, 
then the output should be 
{pos: [], peaks: []}.

'''

def pick_peaks(arr):
    x, y = 0, 0
    p = []
    h = []
    for i in range(1, len(arr)):
        if arr[i] > arr[y]:
            x = y
            y = i
        else:
            if arr[i] < arr[y]:
                if arr[x] < arr[y]:
                    p.append(y)
                    h.append(arr[y])
                x = y
                y = i
    return {'pos': p, 'peaks': h}

'''
Sudoku solution Validator

'''

def valid_solution(board):
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
        if len(set([board[j][i] for j in range(9)])) != 9:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set([board[i+k][j+l] for k in range(3) for l in range(3)])) != 9:
                return False
    return True


'''
function which increments a string, to create a new string.

If the string already ends with a number, 
the number should be incremented by 1.
If the string does not end with a number. 
the number 1 should be appended to the new string.
Examples:

foo -> foo1
foobar23 -> foobar24
'foobar910' should equal 'foobar100'

Attention: If the number has leading zeros 
the amount of digits should be considered.
'''
def increment_string(strng):
    numbers = strng.rstrip('0123456789')
    words = strng[len(numbers):]
    if words == '':
        return numbers + '1'
    else:
        return numbers + str(int(words) + 1).zfill(len(words))

'''
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

Your task is to return the list 
with elements from tree sorted by levels, 
which means the root element goes first, 
then root children (from left to right) 
are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]



'''
def tree_by_levels(node):
    if not node:
        return []
    result = []
    queue = [node]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result




