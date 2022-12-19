class Student{
    public:
    int m[5];
    int sum;

    Student(){
        sum = 0;
    }

    void input(){
        for(int i = 0; i < 5; i++){
            cin>>m[i];
            sum += m[i];    
        }
    }
    
    int calculateTotalScore(){
        return sum;
    }
};
