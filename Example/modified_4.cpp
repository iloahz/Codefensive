#include <cstdio>

int main(){
    int n,i,j,v1,v2,v3;
    v1=100;
    v2=2;
    v3=0;
    n=v1;
    for (i=v2;i<=n;i++){
        for (j=v2;j*j<=i;j++)
            if (i%j==v3) break;
        if (j*j>i) printf("%d\n",i);
    }
    return v3;
}
