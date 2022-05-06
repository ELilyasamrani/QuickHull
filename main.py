import functions as fct
import math
import matplotlib.pyplot as plt
import random

def quickhullBiss(e,A,B,env,oldC=(0,0)) :
    if len(e) == 0:
        C=oldC
        plt.plot([A[0], C[0]], [A[1], C[1]], c="black")
        plt.plot([B[0], C[0]], [B[1], C[1]], c="black")
        return None
    else:
        maxs = fct.surface(e[0],A,B)
        C = e[0]
        for p in e:
            if fct.surface(p,A,B)> maxs :
                maxs = fct.surface(p,A,B)
                C = p
        env.append(C)
        plt.plot([A[0],C[0]],[A[1],C[1]],c="grey")
        plt.plot([B[0], C[0]], [B[1], C[1]],c="grey")
        if C[1]> fct.gety(C[0],*fct.getline(A,B)):
            e1, _ = fct.supinf(A,C,e,env)
            e2, _ = fct.supinf(C, B, e,env)
        else:
            _ , e1 = fct.supinf(A,C,e,env)
            _ , e2 = fct.supinf(C, B, e,env)
        quickhullBiss(e1, A, C, env,C)
        quickhullBiss(e2, C, B, env,C)

def quickhull(Points,env):
    env.clear()
    e1 = []
    e2 = []
    A,B = fct.findLandR(Points,0) #Trouver les points en extremité gauche et droite
    if A[0] == B[0]: #Si tous les points ont le même abscisse
        A, B = fct.findLandR(Points, 1)
    else :
        e1,e2 = fct.supinf(A,B,Points,env) #Subdiviser Points en e1 et e2 telque e1 : ens. des points sup à [AB]
    quickhullBiss(e1,A,B,env) #diviser pour régner : travaillons sur e1
    quickhullBiss(e2, B, A,env) #diviser pour régner : travaillons sur e2
    env.append(A)
    env.append(B)
    plt.plot([A[0],B[0]],[A[1],B[1]],c="green") #Tracer la premiere ligne


if __name__ == "__main__":
    #points = [(x,y) for x in [random.randint(-20,20)*random.random() for _ in range(10) ] for y in [random.randint(0,10)*random.random() for _ in range(10)]]
    points = [(1,3),(2,5.5),(3,4),(4,1.5),(4,4.5),(4,7),(5,3.5),(3,0),(6,-1),(6,2),(6,5.3),(7,1.3),(7.5,6),(8,4),(9,2)]
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.scatter(x,y,c="blue")
    env = []
    quickhull(points,env)
    print(len(env),len(points))
    u = [p[0] for p in env]
    v = [p[1] for p in env]
    plt.scatter(u, v, c="red")
    plt.show()