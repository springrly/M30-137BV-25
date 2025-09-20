t = (1,2,3)
try:
    t[1] = 100
except TypeError:
    print("Error 1")

print(t)

t2 = (4,5)
t3 = t + t2

print(t3, t2.count(3), t2.index(4))