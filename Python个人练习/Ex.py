g = (x*x for x in range(0, 10))
print(g)
print(next(g))
print(next(g))
for i in g:
    print(i, end=' ')
