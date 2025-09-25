#include <bits/stdc++.h>
using namespace std;

void printPattern13(int n)
{
    int counter = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << counter <<" ";
            counter++;
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
        printPattern13(n);
    }
    return 0;
}
