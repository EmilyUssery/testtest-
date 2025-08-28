# import math
from math import pi,sqrt

#print(math.pi)
# TODO DO SOMEHTING
radius= 5
area = pi * radius** 2
print(area)

radius = 3
Vol_sphere = 4/3 * pi * radius**3
print(Vol_sphere)

side_a = 3
side_b = 4
side_c_sq = side_a**2 + side_b**2
side_c = int(sqrt(side_c_sq))

print(side_c)

my_name = "Emily Ussery"
name_len = len(my_name)
print(name_len)

first_name = "Emily"
last_name = "Ussery"
name_len = len(first_name) + len(last_name)
print(name_len)
my_name = first_name +" " + last_name
print(my_name)

my_name_uc = my_name.upper()
my_name_lc = my_name.lower()
print(my_name_uc, my_name_lc)

age = 42
weight = 200
height = 72
print(type(age), type(weight), type(height))

bmi = weight / height **2 * 703

print(bmi)

