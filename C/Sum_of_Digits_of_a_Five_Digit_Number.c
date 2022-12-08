#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    short int digits = 0;
    
    while(n > 0){
        digits += n % 10;
        n /= 10;
    }
    printf("%d", digits);
    return 0;
}
