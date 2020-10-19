p = 11
q = 19
m = p*q

k = 3

i = 0
x = k
while i < 6:
    x = (x**2)% m
    print("x" + str(i) + "= " + str(x))
    i+=1
