diameter = float(input("The diameter of the circle is: "))
pi = 3.14159

radius= diameter / 2
area = pi * radius ** 2
cir = pi * radius * 2

print("\nThe radius of the circle:", radius)
print("The area of the circle:", round(area, 3))
print("The circumference of the circle:", round(cir, 3))