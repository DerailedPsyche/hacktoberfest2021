//Fibonacci series in cpp
#include <iostream>
using namespace std;
void Fibo(int n)
{
     long long int t1 = 0, t2 = 1;
    if (n > 0)
    {
       long long int t3 = t1 + t2;
        t1 = t2;
        t2 = t3;
        cout<< t3;
        Fibo(n - 1);
    }
}
int main()
{
    int n;
    cout<<"Enter the number of terms: "<<endl;
    cin>> n;
    cout<<"Fibonacci Series:"<<endl;
    cout<<0<<" "<< ","<< 1;
    Fibo(n - 2);
    return 0;
}