#include <bits/stdc++.h>
using namespace std;

void printPattern11(int n)
{
    int startValue = 1;

    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
            startValue = 1;
        else
            startValue = 0;
        for (int j = 0; j <= i; j++)
        {
            cout << startValue;
            startValue = 1 - startValue;
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
        printPattern11(n);
    }
    return 0;
}
