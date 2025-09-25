#include <bits/stdc++.h>
using namespace std;

void printPattern12(int n)
{
    int space = 2 * (n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << "Row " << i + 1 << ": ";

        // Right angle triangle
        for (int j = 0; j <= i; j++)
        {
            cout << j + 1;
        }

        // spaces
        for (int j = 1; j <= space; j++)
        {
            cout << " ";
        }

        // left angle triangle
        for (int j = i + 1; j > 0; j--)
        {
            int printedValue = j;
            cout << printedValue;
        }
        cout << endl;

        // Reducing space value by 2
        space -= 2;
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
