#include <bits/stdc++.h>
using namespace std;

int number_reversal(int n)
{
    if (n >= -2 ^ 31 && n <= 2 ^ 31 - 1)
    {
        int r = n % 10;
        n = n / 10;
        while (n != 0)
        {
            r = r * 10 + n % 10;
            n = n / 10;
        }
        return r;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int r = number_reversal(n);
    cout << "Reverse number is: " << r ;
    return 0;
}