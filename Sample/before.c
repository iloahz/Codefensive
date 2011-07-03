void primes(int cap){
    int i, j, composite;
    for(i = 2; i < cap; ++i) {
        composite = 0;
        for(j = 2; j * j < i; ++j) {
            composite += !(i % j);
        }
        if(!composite){
            printf("%dt", i);
        }
    }
}
 
int main(){
    primes(100);
}
