class Rectangle{
    public:
    int width, height;
  
    void read_input(){
        cin>>height;
        cin>>width;
    }
  
    void display(){
        cout<<height<<" "<<width<<endl;
    }
};

class RectangleArea : public Rectangle{
    public:
    void display(){
        cout<<width*height<<endl;
    }
};
