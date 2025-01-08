// -- Directions 
// Given a string, return the character that is most 
// commonly, used in the string. 
// -- Examples 
// maxChar('abccccd') === "c"
// maxChar('apple 12311111') === "1"

function maxChar(str) {
    const charMap = {};
    let max = 0; // Initialize max count
    let maxChar = ''; // Initialize max character

    // Build the character map
    for (let char of str) {
        if (charMap[char]) {
            charMap[char] += 1;
        } else {
            charMap[char] = 1;
        }
    }

    // for(let key in charMap)
    // {
    //     if(charMap[key] > max)
    //     {
    //         max = charMap[key]
    //         maxChar = key
    //     }
    // }

    // Find the character with the maximum count
    for (const [key, value] of Object.entries(charMap)) {
        if (value > max) {
            max = value;
            maxChar = key;
        }
    }

    return maxChar;
}

console.log(maxChar("abcccccccd")); // Output: 'c'
console.log(maxChar("apple 1231111")); // Output: '1'



