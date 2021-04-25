#include <stdio.h>
#include <time.h>

int main(){
 int y, i, n, j, t;

 y = 0;

 for(i = 0; y <= 59450; i++) { 
        t = 0;
        for(j = 1; j <= i; j++) {
            if(i % j == 0) {
                t++;
            }
        }
        if(t == 2) {
            printf("%d\n", i);
        }
        y = clock();
    }
return 0;
}