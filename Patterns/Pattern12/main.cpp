#include <bits/stdc++.h>
using namespace std;

void printPattern12(int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "Row " << i + 1 << ": ";

        // Right angle triangle
        for (int j = 0; j <= i; j++)
        {
            cout << j + 1;
        }

        // spaces
        for (int j = 0; j < (2 * n) - (2 * i + 2); j++)
        {
            cout << " ";
        }

        // left angle triangle
        for (int j = 0; j <= i; j++)
        {
            int printedValue = ((i - j) + 1);
            cout << printedValue;
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
        printPattern12(n);
    }
    return 0;
}
