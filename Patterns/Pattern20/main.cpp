#include <bits/stdc++.h>
using namespace std;

void printPattern20(int n)
{
    int spaceCondition = 2 * n - 2;
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        // stars
        int starsCondition = i;
        if (i > n)
            starsCondition = 2 * n - i;
        for (int j = 0; j < starsCondition; j++)
        {
            cout << "*";
        }

        // spaces

        for (int j = 0; j < spaceCondition; j++)
        {
            cout << " ";
        }

        if (i >= n)
            spaceCondition += 2;
        else
            spaceCondition -= 2;

        // stars
        if (i > n)
            starsCondition = 2 * n - i;
        for (int j = 0; j < starsCondition; j++)
        {
            cout << "*";
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
        printPattern20(n);
    }
    return 0;
}