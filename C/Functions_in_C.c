#include <stdio.h>

int max_of_four(int a, int b, int c, int d) {
        int first =  (a > b)?a:b;
        int second = (c > d)?c:d;
        return (first > second)?first:second;
    }

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    return 0;
}
