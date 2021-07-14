import matplotlib.pyplot as plt
import numpy as np
import collections
u = [[], [], [], [], [], []]
O = 0.4
N = 60
R = [0.2, 0.5, 1, 2, 3, 4]
v = np.linspace(0, N, N)
rg = [0, 1, 2, 3, 4, 5]
def a(n, r):
    n = int(n)
    if n == 0:
        return O
    else:
        x = a(n - 1, r)
        return r * x * (1 - x)

for q in v:
    k = 0
    for k in rg:
        u[k].append(a(q, R[k]))
print("u =",u)

# Тесты

utest = [[], [], []]
Ntest = 5
vtest = np.linspace(0, Ntest, Ntest)
Rtest = [0.2, 0.5, 1]
rgtest = [0,1,2]

for q in vtest:
    k = 0
    for k in rgtest:
        utest[k].append(a(q, Rtest[k]))
print("utest =",utest)

n0 = [0.4, 0.048, 0.009139, 0.001811, 7.2e-05]  #
n1 = [0.4, 0.12, 0.0528, 0.025006, 0.006021]    # посчитанные значения
n2 = [0.4, 0.24, 0.1824, 0.149130, 0.110789]    #

utest0 = [round(t, 6) for t in utest[0]]  #
utest1 = [round(t, 6) for t in utest[1]]  # округление списков для r = 0.2, 0.5, 1 до 6 знаков
utest2 = [round(t, 6) for t in utest[2]]  #

print("utest0 =", utest0, "n0 =", n0)
if collections.Counter(n0) == collections.Counter(utest0):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")

print("utest1 =", utest1, "n1 =", n1)
if collections.Counter(n1) == collections.Counter(utest1):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")

print("utest2 =", utest2, "n2 =", n2)
if collections.Counter(n2) == collections.Counter(utest2):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")

# Графики

plt.figure(dpi=150)
plt.plot(v, u[0], color='m', linewidth=2)
plt.plot(v, u[1], color='b', linewidth=2)
plt.plot(v, u[2], color='g', linewidth=2)
plt.plot(v, u[3], color='r', linewidth=2)
plt.plot(v, u[4], color='y', linewidth=2)
plt.plot(v, u[5], color='black', linewidth=2)
plt.xlabel('n', fontsize=15)
plt.ylabel('x(n)', fontsize=15)
plt.grid()
plt.show()