class MyCalculator implements AdvancedArithmetic{
    @Override
    public int divisor_sum(int n){
        int value = 0;
        for(int i = 1; i <= n; i++){
            if(n % i == 0) value += i;
        }
        return value;
    }
}
