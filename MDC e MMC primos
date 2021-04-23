#include <stdio.h>


int calculo(int N1, int N2);


int main() {
    int N1, N2;
    printf("Digite o primeiro número inteiro:\n");
    scanf("%d\n", &N1);
    printf("Digite o segundo número inteiro:\n");
    scanf("%d\n", &N2);
    calculo(N1, N2);
    
	return 0;
}

int calculo(int N1, int N2){
   int MMC, MDC, num;
    MMC = 0;
    MDC = 1;
    num = 2;
    scanf("%d\n %d\n", &N1, &N2);
     while(N1 != 1 || N2 != 1){
        if(((N1 % num) == 0) && (N1 != 1) && ((N2 % num) == 0) && (N2 != 1) ){
            MMC = MMC + num;
            MDC = MDC * num;
            N1= N1/num;
            N2= N2/num;
            num = 2;
        }else if((N1 % num) == 0 && (N1 != 1)){
           MMC = MMC + num;
           N1= N1/num;
           num = 2;
        }else if((N2 % num) == 0 && N2 != 1){
            MMC = MMC + num;
           N2= N2/num;
           num = 2;
        }else{
            num++;
        }
    }
     printf("MMC: %d\n", MMC);
if(MDC >= 2){
    printf("MDC: %d\n", MDC);
}else{
    printf("MDC: %d\n", 1);
}
    return 0;
}