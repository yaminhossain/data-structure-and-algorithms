#include <bits/stdc++.h>
using namespace std;
void printPattern8(int n)
{
    for (int i = 0; i < n; i++)
    {
        // leftside spaces
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        // stars
        /*  for (int j = 0; j < ((n - i) - 1) * 2 + 1; j++)
         {
             cout << "*";
         }
         */
        // another logic for stars
        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
        {
            cout << "*";
        }

        // rightside spaces
        for (int j = 0; j < i; j++)
        {
            cout << " ";
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
        printPattern8(n);
    }
    return 0;
}