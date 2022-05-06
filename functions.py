"""
 - On considère que chaque point est un tuple (x,y)
"""
import math

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def surface(p1,p2,p3):
    a=distance(p1,p2)
    b=distance(p2,p3)
    c=distance(p1,p3)
    s = (a+ b + c)/2
    if(p2[0]!=p1[0]):
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    else : return 0

def findLandR(E,i):
    max,min = E[0],E[0]
    for p in E:
        if p[i]>max[i]:
            max = p
        elif p[i]<min[i]:
            min = p
    return max,min

def getline(A,B):
    if(A[0]!=B[0]):
        x=(A[1]-B[1])/(A[0]-B[0])
        y= A[1]-x*A[0]
    return (x,y)

def gety(x,a,b):
    return a*x+b

def supinf(A,B,E,env):
    e1,e2=[],[]
    if A[0] != B[0]:
        a, b = getline(A, B)
        for p in E:
            if p != A and p != B:
                if p[1] > gety(p[0], a, b):
                    e1.append(p)
                elif p[1] < gety(p[0], a, b):
                    e2.append(p)
    return e1, e2

