# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from math import sqrt

a=int(input())
b=int(input())

c=a**2+b**2

hyp=sqrt(c)

c1=hyp/2

e=math.atan(c1/b)
f=math.degrees(e)
print(math.ceil(f))
