#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Para Y1' = Y2
double f1(double y2){
    double m;

    m = y2;

    return m;
}

// Para Y2' = (4pi^2)y1 / r^3
double f2(double x1, double y1){
    double m, r, mi;

    r = pow(x1, 2) + pow(y1, 2);
    r = sqrt(r);
    r = pow(r, 3);

    mi = pow(M_PI, 2);
    mi = mi*4;
    mi = mi*y1;

    m = - (mi/r);

    return m;
}

// Para X1' = X2
double f3(double x2){
    double m;

    m = x2;

    return m;
}

// Para X2' = (4pi^2)x1 / r^3
double f4(double x1, double y1){
    double m, r, mi;

    //m = -(4*M_PI*M_PI*x1)/pow( (pow(x1, 2) + pow(y1, 2)) , (3/2) );

    r = pow(x1, 2) + pow(y1, 2);
    r = sqrt(r);
    r = pow(r, 3);

    mi = pow(M_PI, 2);
    mi = mi*4;
    mi = mi*x1;

    m = - (mi/r);

    return m;
}

int main(){
    int n, a = 1;
    double e = 0.2, E, L, mi, r, aux;
    double x1 = a*(1 - e), y1 = 0, x2 = 0, y2 = (2*(M_PI)/sqrt(a))*((sqrt(1+e))/(sqrt(1-e))), h, t = 0, tn = 1;
    double v1, v2, u1, u2;
    double m1, m2, m3, m4;  // Ks do Y1
    double m5, m6, m7, m8;  // Ks do Y2
    double m9, m10, m11, m12;   // Ks do X1
    double m13, m14, m15, m16;  // Ks do X2
    double ma, mb, mc, md;

    FILE *f;

    printf("Informe a quantidade de iteracoes desejada: ");
    scanf("%d",&n);

    h = (double)(tn - t)/n;
    n = 0;
    t = h;

    // Variáveis que guardam os próximos valores de Y1, Y2, X1 e X2
    v1 = y1;
    v2 = y2;
    u1 = x1;
    u2 = x2;

    mi = pow(M_PI, 2);
    mi = mi*4;
    mi = mi*x1;

    r = pow(x1, 2) + pow(y1, 2);
    r = sqrt(r);
    r = pow(r, 3);

    aux = pow(u2, 2) + pow(v2, 2);

    // Calcula a energia e o momento angular da iteração n = 0
    E = aux/2 - mi/r;
    L = u1*v2 + v1*u2;

    f = fopen("x1y1.txt","w+t");
    fprintf(f,"%.8f\t%.8f\n",u1, v1);

    printf("\n\nn\tt\t\tY1\t\tY2\t\tX1\t\tX2\t\tE\t\tL\n");
    printf("%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n", n, t, v1, v2, u1, u2, E, L);

    while(t < tn-h){

        m1 = f1(v2);    // K11 do Y1
        m9 = f3(u2);    // K11 do X1

        m5 = f2(u1, v1);    // K21 do Y2
        m13 = f4(u1, v1);   // K21 do X2

        //printf("K11s\nY1: %f\nY2: %f\nX1: %f\nX2: %f\n", m1, m5, m9, m13);

        m2 = f1(v2+m5*h/2.0);   // K12 do Y1
        m10 = f3(u2+m13*h/2.0); // K12 do X1

        m6 = f2((u1+m9*h/2.0), (v1+m1*h/2.0));     // K22 do Y2
        m14 = f4((u1+m9*h/2.0), (v1+m1*h/2.0));    // K22 do X2



        m3 = f1(v2+m6*h/2.0);   // K13 do Y1
        m11 = f3(u2+m14*h/2.0); // K13 do X1

        m7 = f2((u1+m10*h/2.0), (v1+m2*h/2.0)); // K23 do Y2
        m15 = f4((u1+m10*h/2.0), (v1+m2*h/2.0)); // K23 do X2



        m4 = f1(v2+h*m7);   // K14 do Y1
        m12 = f3(u2+h*m15); // K14 do X1

        m8 = f2((u1+m11*h), (v1+m3*h)); // K24 do Y2
        m16 = f4((u1+m11*h), (v1+m3*h)); // K24 do X2



        ma = ((m1 + 2*m2 + 2*m3 + m4)/6);   // Y1
        mb = ((m5 + 2*m6 + 2*m7 + m8)/6);   // Y2
        mc = ((m9 + 2*m10 + 2*m11 + m12)/6);    // X1
        md = ((m13 + 2*m14 + 2*m15 + m16)/6);   // X2


        // Conta final para o próximo Y1, Y2, X1 e X2
        v1 = v1 + ma*h;
        v2 = v2 + mb*h;
        u1 = u1 + mc*h;
        u2 = u2 + md*h;

        r = pow(x1, 2) + pow(y1, 2);
        r = sqrt(r);
        r = pow(r, 3);

        aux = pow(u2, 2) + pow(v2, 2);

        // Calcula a energia e o momento angular
        E = aux/2 - mi/r;
        L = u1*v2 - v1*u2;

        //fprintf(f,"%d\t%.1f\t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\n", n, t, u1, v1, u2, v2, E, L);
        fprintf(f,"%.8f\t%.8f\n",u1, v1);
        // Auxiliar para a próxima iteração
        t = t + h;
        n++;

        printf("%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n", n, t, v1, v2, u1, u2, E, L);
    }

    fclose(f);
}

