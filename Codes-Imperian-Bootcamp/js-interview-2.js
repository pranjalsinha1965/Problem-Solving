// -- Directions 
// Given an integer, return an integer that is the reverse
// ordering of numbers 

// -- Examples 
// reverseInt(15) === 51
// reverseInt(981) === 189
// reverseInt(500) === 5
// reverseInt(-15) === -51
// reverseInt(-98) === -9

function reverseInt(n) {
    const reverse = n.toString().split('').reverse().join('');
    return parseInt(reverse) * Math.sign(n);
}

console.log(reverseInt(15)); 
console.log(reverseInt(-123));  
console.log(reverseInt(0));  

// -- Directions 
// given a string, return true if the string is a palindrome
// or false if it is not Palindrome are strings that 
// form the same word if it is reversed

// -- Examples 
// palindrome("kayak") === true 
// palindrome("madam") === true 
// palindrome("codingmoney") === false 

function isPalindrome(str) {
    const reversed = str.split('').reverse().join('')
    return str === reversed
}

strings = "Coding Ninjas"
console.log(isPalindrome(strings))

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

// ---  Directions 
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size 
// --- Examples 
// chunk([1, 2, 3, 4], 2) --> [[1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[1, 2, 3, 4, 5], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[1, 2, 3, 4, 5]]

// const { serialize } = require("v8")

function chunk(array, size){
    const result = []
    let index = 0
    while(index<array.length)
    {
        result.push(array.slice(index, index + size))
        index += size
    }
    return result

}

console.log(chunk([1, 2, 3, 4], 2));

// --- Directions 
// write a function that accepts a string. The string should
// capitalize the first letter of each word in the string then 
// return the capitalized string. 
// ---Example 
// capitalize('this is mukhtar from coding money') --> 'This is Mukhtar From Cding Money'
// capitalize('what is titlecase ? ') --> 'What is Titlecase ?'
// capitlaize('titles of books, movies, songs, plays and other works') --> 'Titles Of Books, Movies, Songs, Plays and Other Works'

function capitalize(str) {
    const words = str.split(' ');
    const result = [];

    for (let word of words) {
        // Capitalize the first letter and concatenate with the rest of the word
        result.push(word[0].toUpperCase() + word.slice(1));
    }

    return result.join(' ');
}

console.log(capitalize('this is muktar from coding money'));
// Output: 'This Is Muktar From Coding Money'


// -- Directions
// Given a string, return a new string with the reversed order of characters 
// -- Examples 
// reverse('hi') === 'ih'
// reverse('hello') === 'olleh'
// reverse('CodingMoney') === ''

function reverseFor(str) {
    let reversed = ''
    for (let i=0; i<str.length; i++)
    {
        reversed = str[i] + reversed
    }
    return reversed
}

console.log(reverseFor('Coding Ninjas'))

function reverseRecursive(str) {
    let reversed = ''
    for(let char of str)
    {
        reversed = char + reversed
    }
    return reversed
}
console.log(reverseRecursive('coding Ninjas'))

function reverseMethods(str)
{
    const strToArray = str.split('')
    strToArray.reverse()
    return strToArray.join('')
}
console.log(reverseMethods('coding Ninjas'))