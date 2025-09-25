#include <bits/stdc++.h>
using namespace std;

void printPattern10(int n)
{
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        // cout << i << " ";

        // the variable "stars" will be used instead of "i" as condition
        int stars = i;
        if (i > n)
            stars = 2 * n - i;
        for (int j = 0; j < stars; j++)
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
        printPattern10(n);
    }
    return 0;
}
