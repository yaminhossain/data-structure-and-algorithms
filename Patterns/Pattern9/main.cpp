#include <bits/stdc++.h>
using namespace std;

void firstHalf(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < i * 2 + 1; j++)
        {
            cout << "*";
        }

        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }

        cout << endl;
    }
}

void secondHalf(int n)
{
    for (int i = 0; i < n; i++)
    {
        // leftside spaces
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        // stars
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
        firstHalf(n);
        secondHalf(n);
    }
    return 0;
}