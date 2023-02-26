// JavaScript script to generate all two or more digits numbers such that digits on left are always smaller than digits on right in number

// Main Idea:
//  1. Since all digits are increasing from left to right, largest number we can form is 123456789 which has total 9 digits
//  2. Function generate Numbers will generate all desired numbers which has n digits, so we will call generateNumbers for digits 1 to 9

const numbers = [];
function generateNumbers(start, out, n)
{
    // If number becomes N-digit, append it to list
    if (n == 0)
    {
        numbers.push(out);
        return;
    }

    // start from (prev digit + 1) till 9
    for (let i = start; i <= 9; i++)
    {
        // append current digit to number
        let str = out + i.toString();

        // recurse for next digit
        generateNumbers(i + 1, str, n - 1);
    }
}
 
// Driver code for above function
for(let n = 1; n <= 9; n += 1){
    generateNumbers(1, " ", n);
}

console.log("Total numbers = ", numbers.length);
console.log("Print numbers: ", numbers);