#include <bits/stdc++.h>
using namespace std;

void printPattern22(int n)
{
    for (int i = 0; i < 2 * n - 1; i++)
    {
        for (int j = 0; j < 2 * n - 1; j++)
        {
            int top = i;
            int left = j;
            int bottom = (2 * n - 1) - 1 - i;
            int right = (2 * n - 1) - 1 - j;
            int distance = min(min(top, bottom), min(left, right));
            cout << n - distance << " ";
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
        printPattern22(n);
    }
    return 0;
}