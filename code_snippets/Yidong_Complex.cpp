#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>

/**
 * @brief Generate combinations of numbers that sum up to a target value recursively.
 * 
 * This function generates all possible combinations of numbers that sum up to the given target value.
 * It starts from a specified starting point and recursively generates combinations until the target value is reached.
 * 
 * @param v A string representing the current combination of numbers.
 * @param tgt The remaining target value to achieve.
 * @param start The starting point for choosing numbers.
 */
void Run(const std::string& v, int tgt, int start) {
    // Loop until tgt is greater than or equal to 2 * start + 1
    for (; tgt >= 2 * start + 1; ++start)
        // Recursively call Run with updated values
        Run(v + ' ' + boost::lexical_cast<std::string>(start), tgt - start, start + 1);
    
    // Print the current combination and remaining target value
    std::cout << v << ' ' << tgt << std::endl;
}

int main() {
    // Start the recursive process with empty string, target value 10, and starting point 1
    Run(std::string(), 10, 1);
    
    // Wait for user input to close the program
    getchar();
    return 0;
}
