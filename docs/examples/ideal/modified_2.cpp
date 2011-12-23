#include <cstdio>

int main(){
    int n,i,j;
    n=100;
    for (i=2;i<=n;i++){
        for (j=2;j*j<=i;j++)
             if (i%j==0) break;
        j*j>i ? printf("%d\n",i) : 0;
    }
    return 0;
}
