// This program takes an integer input from the user and finds the N'th prime
// number. It employs a simple algorithm where it iterates through numbers
// starting from 2 and checks each number for primality. It uses a counter 'x'
// to keep track of the prime numbers found so far. The algorithm makes use of
// the fact that prime numbers greater than 2 are odd, so it only checks odd
// numbers beyond 2. The primality check is done by testing divisibility of the
// number by odd numbers up to its square root. If a number is found to be
// prime, 'x' is incremented, and when 'x' reaches the desired count 'N', the
// loop exits, and the N'th prime number is outputted.

#include <iostream>  // Input-output stream objects.
#include <cmath>     // Math functions and constants.
using namespace std;

int main()
{
    int N = 0;  // Variable to store user input.
    int x = 0;  // Counter for prime numbers.
    int i = 2;  // Candidate number for prime checking.

    cout << "Enter integer: " << endl;  // Prompt user for input.
    cin >> N;                           // Read user input.

    while ( x < N )  // Loop until x (count of prime numbers) is less than N.
    {
        if ( i == 2 )  // Special case for the first prime number, 2.
            x ++;      // Increment the count of prime numbers.

        else if ( i > 2 && i % 2 != 0 )  // For odd numbers greater than 2.
        {
            // Check for divisibility up to square root of i,
            // incrementing by 2 (only checking odd numbers).
            for ( int a = 3 ; a <= sqrt( i ) ; a += 2 )
            {
                if ( i % a != 0 )  // If i is not divisible by a.
                    x ++;          // Increment the count of prime numbers.

                else if ( i % a == 0 )  // If i is divisible by a.
                    break;              // Break out of the loop, as i is not a prime number.
            }
        }

        i ++;  // Move to the next number.
    }

    cout << "The "<< N << "'th prime number is : " << i - 1 << endl;  // Output the N'th prime number.
}
