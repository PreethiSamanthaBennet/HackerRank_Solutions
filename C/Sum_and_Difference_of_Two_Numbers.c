#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    
    int e = a + b;
    int f = a - b;
    printf("%d %d\n", e, f);
    
    float c,d;
    scanf("%f %f", &c, &d);
    
    float y = c + d;
    float z = c - d;
    printf("%3.1f %3.1f ", y, z);

    return 0;
}
