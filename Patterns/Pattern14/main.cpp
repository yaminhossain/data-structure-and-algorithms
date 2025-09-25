#include <bits/stdc++.h>
using namespace std;

void printPattern14(int n)
{
    for (int i = 0; i < n; i++)
    {
        
        for (char j = 'A'; j <= 'A' + i; j++)
        {
            cout << j;
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
        printPattern14(n);
    }
    return 0;
}
