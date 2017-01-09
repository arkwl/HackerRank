#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n; 
    int f[20];
    int true[20];
    
    scanf("%d\n", &n);
    for(int i = 0 ; i < n ; i++){
        scanf("%d", &f[i]);
    }
    
    for(int i = 0 ; i < 20 ; i++){
        true[i] = 0;
    }
    
    for(int i = 0 ; i < n ; i++){
        if (true[f[i]] == 0){
            true[f[i]] = 1;
        }
        else{
            printf("NO\n");
            return 0;
        }  
    }
    printf("YES\n");
    return 0;
}