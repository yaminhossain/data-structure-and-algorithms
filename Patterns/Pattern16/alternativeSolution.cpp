#include <bits/stdc++.h>
using namespace std;

void printPattern16(int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << ": ";
        char printingCharacter = 'A' + i;

        for (char j = 'A'; j <= 'A' + i; j++)
        {
            cout << printingCharacter << " ";
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
        printPattern16(n);
    }
    return 0;
}