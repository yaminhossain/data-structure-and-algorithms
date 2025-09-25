#include <bits/stdc++.h>
using namespace std;

void printPattern15(int n)
{
    for (int i = 1; i <= n; i++)
    {
        cout << "Row " << i << ": ";
        for (char j = 'A'; j <= 'A' + (n - i); j++)
        {
            cout << j << " ";
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
        printPattern15(n);
    }
    return 0;
}
