j = 1
n = int(input("wprowadz n:"))
pi = 0
for i in range(n):
    if i % 2 == 0:
        pi += 4 / j
    else:
        pi -= 4 / j
    j += 2
print(pi)