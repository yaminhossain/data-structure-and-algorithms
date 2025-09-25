#include <bits/stdc++.h>
using namespace std;
void printPattern4(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <=i; j++)
        {
            cout << i+1 << " ";
        }
        cout << endl;
    }
}

int main()
{
    cout << "Number of test cases:\n";
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cout << "Rows:";
        int n;
        cin >> n;
        printPattern4(n);
    }
    return 0;
}