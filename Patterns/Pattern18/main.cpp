#include <bits/stdc++.h>
using namespace std;

void printPattern18(int n)
{
    for (int i = 0; i < n; i++)
    {
        char initialCharacter = ('A' + n)-1;
        for (int j = i; j >= 0; j--)
        {
            char printingCharacter = initialCharacter - j;
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
        printPattern18(n);
    }
    return 0;
}