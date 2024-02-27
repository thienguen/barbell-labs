#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N = 0;
    int x = 0;
    int i = 2;

    cout << "Enter integer: " << endl;
    cin >> N;

    while ( x < N )
    {
        if ( i == 2 )
            x ++;

        else if ( i > 2 && i % 2 != 0 )
        {
            for ( int a = 3 ; a <= sqrt( i ) ; a += 2 )
            {
                if ( i % a != 0 )
                    x ++;                         // Incorrect              
                else if ( i % a == 0 )
                    break;
            }
        }

        i ++;
    }

    cout << "The "<< N << "'th prime number is : " << i - 1 << endl;

}