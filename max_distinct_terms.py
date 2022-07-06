# algorithm designed to split a number into the maximum number of distinct terms

n = int(input())
# list of terms
terms = []
# k is the number of terms
k = 0
i = 1
# while our number still exists, check whether or not next consecutive -i- is
# suitable for substraction
while n:
    if n - i == 0 or n - i >= i + 1:
        n -= i
        k += 1
        terms.append(i)
    i += 1

# print number of terms and terms themselves in ascending order
print(k)
print(*terms)

# speed - O(n), where n is our number