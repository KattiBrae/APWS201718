import sympy


K= 1.14
p= 1
#N = 1/(K-1)*(pb*(pa/pb)**(1/k)-pa)*1/p*ma



t = 1
pa = 2.5
pb = 7.2
ma = 0.96792972684347
N = 1/(K-1)*(pb*(pa/pb)**(1/K)-pa)*1/p*ma
print(N)

t = 6
pa =  3.1
pb =  9
ma =  1.2236833712185382
N = 1/(K-1)*(pb*(pa/pb)**(1/K)-pa)*1/p*ma
print(N)


t =   12
pa =  3.2
pb =  11.5
ma = 1.2205475539195096
N = 1/(K-1)*(pb*(pa/pb)**(1/K)-pa)*1/p*ma
print(N)

t =   18
pa =  3.2
pb =  13.9
ma = 0.04410295345510843
N = 1/(K-1)*(pb*(pa/pb)**(1/K)-pa)*1/p*ma
print(N)


print('Fehler')

ma  = sympy.var('ma')
f =  1/(K-1)*(pb*(pa/pb)**(1/K)-pa)*1/p*ma
df =  sympy.sqrt((f.diff(ma)*0.000460867120745500 )**2)
print(df)
df =  sympy.sqrt((f.diff(ma)*0.000467681498406329)**2)
print(df)
df =  sympy.sqrt((f.diff(ma)*0.000488124631388814)**2)
print(df)
df =  sympy.sqrt((f.diff(ma)*0.000520044610957958)**2)
print(df)
