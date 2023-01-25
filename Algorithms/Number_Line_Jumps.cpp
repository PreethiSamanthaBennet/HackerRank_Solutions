string kangaroo(int x1, int v1, int x2, int v2) {
    double res = (double)(x1 - x2)/(v2 - v1);
    
    if(res == floor(res) && res >= 0)
        return string("YES");
    return("NO");
}
