Complex operator +(const Complex &c1,const Complex &c2){
    return {(c1.a+c2.a), (c1.b+c2.b)};
}

ostream& operator<<(ostream &os, const Complex c){
    string sign;

    if(c.b < 0){
        sign = "-";
    }
    sign = "+";

    return os<<c.a<<sign<<"i"<<c.b;
}
