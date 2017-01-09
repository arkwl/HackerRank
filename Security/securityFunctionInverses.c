#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n; 
    int f[20];
    int final[20];
    
    scanf("%d\n", &n);
    for(int i = 0 ; i < n ; i++){
        scanf("%d", &f[i]);
    }
    
    for(int i = 0 ; i < 20 ; i++){
        final[i] = 0;
    }
    
    for(int i = 0 ; i < n ; i++){
        int temp = f[i];
        //printf("temp: %d fI %d\n",temp, i + 1);
        final[temp] = i + 1;
    }
    
    for(int i = 1 ; i <= n ; i++){
        printf("%d\n", final[i]);
    }
    return 0;
}