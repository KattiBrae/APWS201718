import sympy



x = sympy.var('x')

a=5.19865841e-03
b=-1.37538700e-01
c=-5.41834365e-01
d=2.96917157e+02



f=a*x**3+b*x**2+c*x+d
print(f.diff(x))




x = 0

while x<18:

    f2=0.01559597523*x**2 - 0.2750774*x - 0.541834365
    print(f2)
    x = x+1

print("fertig")
