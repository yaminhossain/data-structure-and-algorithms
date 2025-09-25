#include <bits/stdc++.h>
using namespace std;

void printPattern2(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <=i; j++)
        {
            cout << "* ";
        }

        cout << "\n";
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
        printPattern2(n);
    }
    return 0;
}