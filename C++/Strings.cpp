#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    string b;
    
    cin>>a;
    cin>>b;

    int len1 = a.size();
    int len2 = b.size();

    cout<<len1<<" "<<len2;

    string c = a+b;

    cout<<endl;
    
    cout<<c;
    
    cout<<endl;
    
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;

    cout<<a<<" "<<b;
    return 0;
}
