with open ('mat1.txt', 'r') as spldv:
    equ = [[int(num)for num in line.split(',')]for line in spldv]

def eliminasi_Y(equ):
    n = equ
    print((n[0][0]*n[0][4]-n[0][1]*n[0][3]),'x =',(n[0][2]*n[0][4]-n[0][1]*n[0][5]))
    print('X =',(n[0][2]*n[0][4]-n[0][1]*n[0][5])/(n[0][0]*n[0][4]-n[0][1]*n[0][3]))

def solution_Y(equ):
    n = equ
    x = (n[0][2]*n[0][4]-n[0][1]*n[0][5])/(n[0][0]*n[0][4]-n[0][1]*n[0][3])
    print('Y =',n[0][2]/n[0][1],'-',n[0][0]/n[0][1],'X')
    print('Y =',(n[0][2]/n[0][1])-(n[0][0]/n[0][1])*x)

def Solution_spldv(equ):
    n = equ
    x = (n[0][2]*n[0][4]-n[0][1]*n[0][5])/(n[0][0]*n[0][4]-n[0][1]*n[0][3])
    y = (n[0][2]/n[0][1])-(n[0][0]/n[0][1])*x
    print('X =',x)
    print('Y =',y)

print('Data of Equation : ')
print('[[a, b, c, p, q, r]]')
print(equ)
print('------------------------------')
print('aX + bY = c')
print('pX + qY = r')
print('-------------------------------')
print(equ[0][0],'X +',equ[0][1],'Y =',equ[0][2])
print(equ[0][3],'X +',equ[0][4],'Y =',equ[0][5])
print('')
print('Solution of two varibles')
print(equ[0][0],'X +',equ[0][1],'Y =',equ[0][2], '|x',equ[0][4])
print(equ[0][3],'X +',equ[0][4],'Y =',equ[0][5], '|x',equ[0][1])
print('__________________________________\n ')
print((equ[0][0]*equ[0][4]),'X +',(equ[0][1]*equ[0][4]),'Y =',equ[0][2]*equ[0][4])
print((equ[0][1]*equ[0][3]),'X +',(equ[0][1]*equ[0][4]),'Y =',equ[0][1]*equ[0][5])
print('___________________________________ - \n')
eliminasi_Y(equ)
print('___________________________________ \n')
solution_Y(equ)
print('------------------------------------')
Solution_spldv(equ)