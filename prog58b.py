import math
va = int(input("A:"))
vb = int(input("B:"))
vc = int(input("C:"))

vd = vb ** 2 - 4 * va * vc

rone = (-vb + math.sqrt(vd)) / (2 * va)
rtwo = (-vb - math.sqrt(vd)) / (2 * va)

print(rone)
print(rtwo)