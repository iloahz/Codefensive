#include <cstdio>

int main(){
    int n,i,j;
    n=100;
    for (i=2;i<=n;i++){
        for (j=2;j*j<=i;j++)
            if (i%j==0) break;
        if (j*j>i) printf("%d\n",i);
    }
    return 0;
}

