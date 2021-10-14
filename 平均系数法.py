# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 08:20:53 2021

@author: wxj01
"""

#exec()一个字符串可以运行那个字符串对应的问题

#这里所有/要变成\

A=[4,2,2,2,8,4,2,4,4]
U=[16,28,40]
V=[16,28,40]
O=[8,14,10,0]
D=O
T=[32,0]
X=84
#三行，迭代次数
q=[[4,2,2],[2,8,4],[2,4,4],0]
#下标1，下标2，迭代次数，具体值
q11=[1,1,0,0]
q12=[1,2,0,0]
q13=[1,3,0,0]
q21=[2,1,0,0]
q22=[2,2,0,0]
q23=[2,3,0,0]
q31=[3,1,0,0]
q32=[3,2,0,0]
q33=[3,3,0,0]
Li1=[0,0]
Li2=[0,0]
Li3=[0,0]
Lj1=[0,0]
Lj2=[0,0]
Lj3=[0,0]
Li=[]
Lj=[]
#代入初始数据
for i in range(3):
    for j in range(3):
        exec('q'+str(i+1)+str(j+1)+'[3]=A['+str(3*i+j)+']')
FO=[0,0,0,0]
FD=[0,0,0,0]
G=[0,0]

# #L38-L152为平均增长系数法
# print('求发生交通量增长系数和吸引交通量增长系数')
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1


# print('第一次近似')
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=0.5*(FO['+str(i)+']+FD['+str(j)+'])*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=\\frac{F_{O'+str(i+1)+'}+F_{D'+str(j+1)+'}}{2}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('重新计算增长系数')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1


# print('第二次近似')
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=0.5*(FO['+str(i)+']+FD['+str(j)+'])*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=\\frac{F_{O'+str(i+1)+'}+F_{D'+str(j+1)+'}}{2}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('重新计算增长系数')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1


# print('第三次近似')
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=0.5*(FO['+str(i)+']+FD['+str(j)+'])*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=\\frac{F_{O'+str(i+1)+'}+F_{D'+str(j+1)+'}}{2}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('重新计算增长系数')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1


# print('第四次近似')
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=0.5*(FO['+str(i)+']+FD['+str(j)+'])*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=\\frac{F_{O'+str(i+1)+'}+F_{D'+str(j+1)+'}}{2}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('重新计算增长系数')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1




# #L156-219为底特律
# print('$求发生交通量增长系数和吸引交通量增长系数$\\\\')
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1



# print('$第一次近似$\\\\')
# G[0]=T[0]/X
# print('G^{'+str(G[1])+'}=\\frac{T^{'+str(T[1])+'}}{X}='+str(G[0])+'\\\\')
# G[1]+=1
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=FO['+str(i)+']*FD['+str(j)+']*G[0]*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{O'+str(i+1)+'}*F_{D'+str(j+1)+'}*G[0]*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('$重新计算增长系数$\\\\')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# T[0]=O[0]+O[1]+O[2]
# FO[3]+=1
# FD[3]+=1
# T[1]+=1


# print('$第二次近似$\\\\')
# G[0]=T[0]/X
# print('G^{'+str(G[1])+'}=\\frac{T^{'+str(T[1])+'}}{X}='+str(G[0])+'\\\\')
# G[1]+=1
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=FO['+str(i)+']*FD['+str(j)+']*G[0]*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{O'+str(i+1)+'}*F_{D'+str(j+1)+'}*G[0]*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('$重新计算增长系数$\\\\')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1



# #L217-271为福莱特
# print('$求发生交通量增长系数和吸引交通量增长系数$\\\\')
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1


# print('$求L_i,L_j$\\\\')
# for k in range(3):
#     exec('Li'+str(k+1)+'[0]=(O[k])/(FD[0]*q'+str(k+1)+'1[3]+FD[1]*q'+str(k+1)+'2[3]+FD[2]*q'+str(k+1)+'3[3])')
#     exec('Lj'+str(k+1)+'[0]=(O[k])/(FD[0]*q1'+str(k+1)+'[3]+FD[1]*q2'+str(k+1)+'[3]+FD[2]*q3'+str(k+1)+'[3])')
#     exec('Li.append(Li'+str(k+1)+')')
#     exec('Lj.append(Lj'+str(k+1)+')')
#     exec('Li'+str(k+1)+'[1]+=1')
#     exec('Lj'+str(k+1)+'[1]+=1')
#     print('L_{i'+str(k+1)+'}^{'+str(FO[3]-1)+'}=\\frac{O_{'+str(k+1)+'}}{F_{D1}^{'+str(FO[3]-1)+'}*q_{'+str(k+1)+'1}^{'+str(FO[3]-1)+'}+F_{D2}^{'+str(FO[3]-1)+'}*q_{'+str(k+1)+'2}^{'+str(FO[3]-1)+'}+F_{D3}^{'+str(FO[3]-1)+'}*q_{'+str(k+1)+'3}^{'+str(FO[3]-1)+'}}='+str(Li[k][0])+'\\\\')
#     print('L_{j'+str(k+1)+'}^{'+str(FO[3]-1)+'}=\\frac{D_{'+str(k+1)+'}}{F_{O1}^{'+str(FO[3]-1)+'}*q_{1'+str(k+1)+'}^{'+str(FO[3]-1)+'}+F_{O2}^{'+str(FO[3]-1)+'}*q_{2'+str(k+1)+'}^{'+str(FO[3]-1)+'}+F_{O3}^{'+str(FO[3]-1)+'}*q_{3'+str(k+1)+'}^{'+str(FO[3]-1)+'}}='+str(Lj[k][0])+'\\\\')




# print('第一次近似')
# for i in range(3):
#     for j in range(3):
#         exec('q'+str(i+1)+str(j+1)+'[3]=FO['+str(i)+']*FD['+str(j)+']*0.5*(Li[i][0]+Lj[j][0])*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
#         exec('q'+str(i+1)+str(j+1)+'[2]+=1')
#         exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
#         print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{O'+str(i+1)+'}*F_{D'+str(j+1)+'}*\\frac{F_{O'+str(i+1)+'}+F_{D'+str(j+1)+'}}{2}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
# q[3]+=1
# print(q)


# print('$重新计算增长系数$\\\\')
# for i in range(3):
#     O[i]=q[i][0]+q[i][1]+q[i][2]
#     D[i]=q[0][i]+q[1][i]+q[2][i]
# for i in range(3):
#     FO[i]=U[i]/O[i]
#     FD[i]=V[i]/D[i]
#     print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
#     print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
# FO[3]+=1
# FD[3]+=1

#L273-330为佛尼斯
print('求发生交通量增长系数和吸引交通量增长系数')
for i in range(3):
    FO[i]=U[i]/O[i]
    FD[i]=V[i]/D[i]
    print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
    print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
FO[3]+=1
FD[3]+=1


print('第一次近似')
for i in range(3):
    for j in range(3):
        exec('q'+str(i+1)+str(j+1)+'[3]=FO['+str(i)+']*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
        exec('q'+str(i+1)+str(j+1)+'[2]+=1')
        exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
        print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{O'+str(i+1)+'}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
q[3]+=1
print(q)


print('重新计算增长系数')
for i in range(3):
    O[i]=q[i][0]+q[i][1]+q[i][2]
    D[i]=q[0][i]+q[1][i]+q[2][i]
for i in range(3):
    FO[i]=U[i]/O[i]
    FD[i]=V[i]/D[i]
    print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
    print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
FO[3]+=1
FD[3]+=1

print('第二次近似')
for i in range(3):
    for j in range(3):
        exec('q'+str(i+1)+str(j+1)+'[3]=FD['+str(j)+']*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
        exec('q'+str(i+1)+str(j+1)+'[2]+=1')
        exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
        print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{D'+str(j+1)+'}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
q[3]+=1
print(q)


print('重新计算增长系数')
O[0]=q[0][0]+q[0][1]+q[0][2]
O[1]=q[1][0]+q[1][1]+q[1][2]
O[2]=q[2][0]+q[2][1]+q[2][2]
# D[0]=q[0][0]+q[1][0]+q[2][0]
# D[1]=q[0][1]+q[1][1]+q[2][1]
# D[2]=q[0][2]+q[1][2]+q[2][2]
D=[16,28,40,0]
for i in range(3):
    FO[i]=U[i]/O[i]
    FD[i]=V[i]/D[i]
    print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
    print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
FO[3]+=1
FD[3]+=1


print('第三次近似')
for i in range(3):
    for j in range(3):
        exec('q'+str(i+1)+str(j+1)+'[3]=FO['+str(i)+']*q'+str(i+1)+str(j+1)+'[3]')#这一行里有增长函数
        exec('q'+str(i+1)+str(j+1)+'[2]+=1')
        exec('q['+str(i)+']['+str(j)+']=q'+str(i+1)+str(j+1)+'[3]')        
        print('q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2])+'=F_{O'+str(i+1)+'}*q_{'+str(i+1)+str(j+1)+'}^'+str(q11[2]-1)+'='+str(q[i][j])+'\\\\')
q[3]+=1
print(q)


print('重新计算增长系数')
for i in range(3):
    O[i]=q[i][0]+q[i][1]+q[i][2]
    D[i]=q[0][i]+q[1][i]+q[2][i]
for i in range(3):
    FO[i]=U[i]/O[i]
    FD[i]=V[i]/D[i]
    print('F_{O'+str(i+1)+'}^'+str(FO[3])+'=\\frac{U_'+str(i+1)+'}{O_'+str(i+1)+'}='+str(FO[i])+'\\\\')
    print('F_{D'+str(i+1)+'}^'+str(FO[3])+'=\\frac{V_'+str(i+1)+'}{D_'+str(i+1)+'}='+str(FD[i])+'\\\\')
FO[3]+=1
FD[3]+=1































