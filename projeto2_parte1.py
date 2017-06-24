import math

r_f = lambda x, y: math.sqrt(x**2 + y**2)**3
mi_f = lambda v: (math.pi**2)*4*v

def main():
    n = a = tn = 1
    e = y1 = x2 = t = 0
    y2 = (2*(math.pi)/math.sqrt(a))*((math.sqrt(1+e))/(math.sqrt(1-e)))
    x1 = 1
    
    escolha = int(input("Informe a quantidade de iterações: "))
    
    h = (tn - t)/escolha
    escolha = 0
    t = h
    
    v1, v2, u1, u2 = y1, y2, x1, x2
    
    mi = mi_f(x1)
    r = r_f(x1, y1)
    
    aux = u2**2 + v2**2
    
    E = aux/2 - mi/r
    L = u1*v2 + u2*v1
    print("\n\nn\tt\tY1\tY2\tX1\tX2\tE\t\tL\n")
    print("{}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.8f}\t{:0.8f}".format(escolha, t, v1, v2, u1, u2, E, L))
    
    while(t < tn-h):
        m1 = v2
        m9 = u2
        
        m5 = f(u1, v1)
        m13 = f(v1, u1)
        
        m2 = v2+m5*h/2.0
        m10 = u2+m13*h/2.0
        
        m6 = f((u1+m9*h/2.0), (v1+m1*h/2.0))
        m14 = f((v1+m1*h/2.0), (u1+m9*h/2.0))
        
        m3 = v2+m6*h/2.0
        m11 = u2+m14*h/2.0
        
        m7 = f((u1+m10*h/2.0), (v1+m2*h/2.0))
        m15 = f((v1+m2*h/2.0), (u1+m10*h/2.0))
        
        m4 = v2+h*m7
        m12 = u2+h*m15
        
        m8 = f(u1+m11*h, v1+m3*h)
        m16 = f(v1+m3*h, u1+m11*h)
        
        ma = ((m1 + 2*m2 + 2*m3 + m4)/6)
        mb = ((m5 + 2*m6 + 2*m7 + m8)/6)
        mc = ((m9 + 2*m10 + 2*m11 + m12)/6)
        md = ((m13 + 2*m14 + 2*m15 + m16)/6)
        
        v1 += ma*h
        v2 += mb*h
        u1 += mc*h
        u2 += md*h
        
        r = r_f(x1, y1)
        aux = u2**2 + v2**2
        
        E = aux/2 - mi/r
        L = u1*v2 - v1*u2
        
        t += h
        escolha += 1
        
        print("{}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.4f}\t{:0.8f}\t{:0.8f}".format(escolha, t, v1, v2, u1, u2, E, L))
        
#f2 = f(x1, y1)
#f4 = f(y1, x1)
def f(a, b):
    r = r_f(a, b)
    mi = mi_f(b)
    
    return (-(mi/r))

main()