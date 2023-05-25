#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[1000];
    int digits[10] = {0};
    scanf("%s", str);

    for(int i = 0; i < strlen(str); i++){
        if(str[i] >= 48 && str[i] <= 57){
            digits[str[i] - 48]++;
        }
    }
    
    for(int i = 0; i < 10; i++){
        printf("%d ", digits[i]);
    }
    return 0;
}
