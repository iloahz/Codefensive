#include <cstdio>

void f2(int &j,int &i){
    if ((j*j<=i)==0) return;
    if (i%j==0) return;
    j++;
    f2(j,i);
}

void f1(int &i,int &n){
    if ((i<=n)==0) return;
    int j;
    j=2;
    f2(j,i);
    if (j*j>i) printf("%d\n",i);
    int i_,n_;
    i++;
    f1(i,n);
}

int main(){
    int n,i,j;
    i=2;
    n=100;
    f1(i,n);
    return 0;
}
