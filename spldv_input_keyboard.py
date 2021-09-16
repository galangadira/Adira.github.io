#search a solution for linear algebra 2 and 3 variables
#16 september 2021

print("Persamaan 1 : ax +by= c")
print("Input")
print("Masukkan nilai a, b, dan c")
a = float(input('a :'))
b = float(input('b :'))
c = float(input('c :'))
print("Persamaan 2 : px+qy = r")
print("input")
print("Masukkan niali p, q, dan r")
p = float(input('p :'))
q = float(input('q :'))
r = float(input('r :'))

#process 
x = (c*q-b*r)/(a*q-b*p)
y = (1/b)*(c-a*x)

#result
print('')
print('Solution SPLDV :')
print('x :', x)
print('y :', y)